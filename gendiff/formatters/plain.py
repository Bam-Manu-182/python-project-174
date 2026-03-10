def to_str(value):
    if isinstance(value, (dict, list)):
        return "[complex value]"

    if isinstance(value, bool):
        return str(value).lower()

    if value is None:
        return "null"

    if isinstance(value, str):
        return f"'{value}'"

    return str(value)


def render_plain(diff_tree, path=""):
    lines = []

    for node in diff_tree:
        property_name = (
            f"{path}{node['key']}" if path else node['key'])
        node_type = node['type']

        if node_type == 'nested':
            lines.append(
                render_plain(node['children'], property_name))

        elif node_type == 'added':
            lines.append(
                (f"Property '{property_name}' was added "
                 f"with value: {to_str(node['value'])}"))

        elif node_type == 'removed':
            lines.append(
                (f"Property '{property_name}' was removed"))

        elif node_type == 'changed':
            old_val = to_str(node['old_value'])
            new_val = to_str(node['new_value'])
            lines.append(
                (f"Property '{property_name}' was updated. "
                 f"From {old_val} to {new_val}"))

    return "\n".join(lines)
