"""Standard-library contract helpers. No writes, network, or general YAML/Schema engine."""
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlparse

PACKAGE = Path(__file__).resolve().parents[1]


def schema():
    return json.loads((PACKAGE / 'schemas/review-manifest.schema.json').read_text())


def check_shape(value, rule, root, path='$'):
    """Validate only the documented JSON Schema subset used by this package."""
    errors = []
    if '$ref' in rule:
        pointer = rule['$ref']
        if not pointer.startswith('#/'):
            return [f'{path}: unsupported nonlocal $ref']
        target = root
        for key in pointer[2:].split('/'):
            target = target[key]
        return check_shape(value, target, root, path)
    if 'anyOf' in rule:
        if not any(not check_shape(value, option, root, path) for option in rule['anyOf']):
            errors.append(f'{path}: does not match any allowed shape')
        return errors
    types = {'object': dict, 'array': list, 'string': str, 'boolean': bool,
             'null': type(None), 'integer': int, 'number': (int, float)}
    if 'type' in rule:
        allowed = rule['type'] if isinstance(rule['type'], list) else [rule['type']]
        if not any(isinstance(value, types[t]) and not (isinstance(value, bool) and t in ('integer', 'number')) for t in allowed):
            return [f'{path}: wrong type, expected {allowed}']
    if 'const' in rule and value != rule['const']:
        errors.append(f'{path}: expected constant {rule["const"]!r}')
    if 'enum' in rule and value not in rule['enum']:
        errors.append(f'{path}: value outside enum')
    if isinstance(value, str):
        if len(value.strip()) < rule.get('minLength', 0):
            errors.append(f'{path}: blank required text')
        if 'pattern' in rule and not re.search(rule['pattern'], value):
            errors.append(f'{path}: pattern mismatch')
    if isinstance(value, list):
        if len(value) < rule.get('minItems', 0):
            errors.append(f'{path}: too few items')
        if rule.get('uniqueItems') and len({json.dumps(x, sort_keys=True) for x in value}) != len(value):
            errors.append(f'{path}: duplicate entries')
        for i, child in enumerate(value):
            errors.extend(check_shape(child, rule.get('items', {}), root, f'{path}[{i}]'))
    if isinstance(value, dict):
        for key in rule.get('required', []):
            if key not in value:
                errors.append(f'{path}: missing {key}')
        props = rule.get('properties', {})
        for key, child in value.items():
            if key in props:
                errors.extend(check_shape(child, props[key], root, f'{path}.{key}'))
            elif rule.get('additionalProperties') is False:
                errors.append(f'{path}: unknown field {key}')
            elif isinstance(rule.get('additionalProperties'), dict):
                errors.extend(check_shape(child, rule['additionalProperties'], root, f'{path}.{key}'))
    return errors


def contained(root, relative):
    p = Path(relative)
    if p.is_absolute() or '..' in p.parts:
        raise ValueError('artifact path must be relative without traversal')
    resolved = (root / p).resolve()
    if not resolved.is_relative_to(root.resolve()):
        raise ValueError('artifact escapes review root (possibly symlink)')
    return resolved


def comment_json(text, name):
    matches = re.findall(r'<!--\s*' + re.escape(name) + r'\s*\n(.*?)\n\s*-->', text, re.S)
    if len(matches) != 1:
        raise ValueError(f'exactly one {name} block required')
    data = json.loads(matches[0])
    if not isinstance(data, dict):
        raise ValueError(f'{name} must be an object')
    return data


def summary(manifest):
    return {'stage': manifest['stage'], 'versions': manifest['versions'],
            'active_cards': manifest['active_cards'],
            'decision_states': {k: {f: d[f] for f in schema()['x-contract']['decision_summary_fields']}
                                for k, d in manifest['decisions'].items()}}


def markdown_links(text):
    # Inline links/images plus reference definitions; ignore code fences.
    clean = re.sub(r'```.*?```', '', text, flags=re.S)
    pairs = re.findall(r'!?\[([^\]]*)\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+["\'][^)]*)?\)', clean)
    pairs += re.findall(r'^\[([^\]]+)\]:\s*(<[^>]+>|\S+)', clean, re.M)
    return [(label, target.strip('<>')) for label, target in pairs]


def link_errors(root, path, text, external=()):
    errors = []
    for label, target in markdown_links(text):
        parsed = urlparse(target)
        if parsed.scheme in ('http', 'https', 'mailto'):
            continue
        if not parsed.path and not parsed.fragment:
            continue
        location = unquote(parsed.path)
        resolved = (path.parent / location).resolve() if location else path.resolve()
        if parsed.scheme or not resolved.is_relative_to(root.resolve()):
            if 'external' not in label.lower() or target not in external and location not in external:
                errors.append(f'{path.name}: undeclared external link {target}')
        elif not resolved.is_file():
            errors.append(f'{path.name}: broken local link {target}')
        elif parsed.fragment and resolved.suffix.lower() == '.md':
            body = resolved.read_text(encoding='utf-8')
            anchors = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', body))
            counts = {}
            for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', body, re.M):
                slug = re.sub(r'[^\w\- ]', '', heading.lower()).replace(' ', '-')
                count = counts.get(slug, 0); counts[slug] = count + 1
                anchors.add(slug + ('-' + str(count) if count else ''))
            if unquote(parsed.fragment) not in anchors:
                errors.append(f'{path.name}: broken Markdown anchor {target}')
    return errors
