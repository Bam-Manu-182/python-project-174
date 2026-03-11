def stringify(value, depth):
    if not isinstance(value, dict):
        if isinstance(value, bool):
            return str(value).lower()

        if value is None:
            return 'null'

        return str(value)

    indent = " " * (depth * 4)
    child_indent = " " * ((depth + 1) * 4)
    lines = []

    for key, val in value.items():
        lines.append(f"{child_indent}{key}: {stringify(val, depth + 1)}")

    result = "\n".join(lines)

    return f"{{\n{result}\n{indent}}}"


def render_stylish(diff_tree, depth=1):
    indent = " " * (depth * 4)
    prefix_indent = indent[:-2]
    lines = []

    for node in diff_tree:
        key = node['key']
        node_type = node['type']

        if node_type == 'nested':
            val = render_stylish(node['children'], depth + 1)
            lines.append(f"{indent}{key}: {val}")

        elif node_type == 'added':
            val = stringify(node['value'], depth)
            lines.append(f"{prefix_indent}+{key}: {val}")

        elif node_type == 'removed':
            val = stringify(node['value'], depth)
            lines.append(f"{prefix_indent}-{key}: {val}")

        elif node_type == 'unchanged':
            val = stringify(node['value'], depth)
            lines.append(f"{indent}{key}: {val}")

        elif node_type == 'changed':
            old_val = stringify(node['old_value'], depth)
            new_val = stringify(node['new_value'], depth)
            lines.append(f"{prefix_indent}- {key}: {old_val}")
            lines.append(f"{prefix_indent}+ {key}: {new_val}")

    result = "\n".join(lines)
    closing_indent = " " * ((depth - 1) * 4)
    return f"{{\n{result}\n{closing_indent}}}"
