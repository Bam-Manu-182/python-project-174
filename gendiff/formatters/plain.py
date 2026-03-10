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
        key = node.get('key')
        node_type = node.get('type')
        property_name = f"{path}{key}"

        if node_type == 'nested':
            lines.append(render_plain(node.get('children'), f"{property_name}."))

        elif node_type == 'added':
            msg = f"Property '{property_name}' was added with value: "
            lines.append(f"{msg}{to_str(node.get('value'))}")

        elif node_type == 'removed':
            lines.append(f"Property '{property_name}' was removed")

        elif node_type == 'changed':
            msg = f"Property '{property_name}' was updated. From "
            val1 = to_str(node.get('old_value'))
            val2 = to_str(node.get('new_value'))
            lines.append(f"{msg}{val1} to {val2}")

    return "\n".join(lines)
