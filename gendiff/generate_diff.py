from gendiff.parsers import get_data


def stringify(value, depth):
    if not isinstance(value, dict):
        if isinstance(value, bool):
            return str(value).lower()

        if value is None:
            return 'null'

        return str(value)

    current_indent = "    " * (depth + 1)
    closing_indent = "    " * depth
    lines = []

    for key, val in value.items():
        lines.append(f"{current_indent}{key}: {stringify(val, depth + 1)}")
        result = "\n".join(lines)

        return f"{{\n{result}\n{closing_indent}}}"


def build_diff(data1, data2, depth=1):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    indent = "    " * depth
    prefix_indent = indent[:-2]
    lines = []

    for key in keys:
        val1 = data1.get(key)
        val2 = data2.get(key)

        if isinstance(val1, dict) and isinstance(val2, dict):
            lines.append(f"{indent}{key}: {build_diff(val1, val2, depth + 1)}")

        elif key in data1 and key in data2 and val1 == val2:
            lines.append(f"{indent}{key}: {stringify(val1, depth)}")

        elif key in data1 and key in data2:
            lines.append(f"{prefix_indent}- {key}: {stringify(val1, depth)}")
            lines.append(f"{prefix_indent}+ {key}: {stringify(val2, depth)}")

        elif key in data1:
            lines.append(f"{prefix_indent}- {key}: {stringify(val1, depth)}")

        else:
            lines.append(f"{prefix_indent}+ {key}: {stringify(val2, depth)}")

    result = "\n".join(lines)
    closing_indent = "    " * (depth - 1)

    return f"{{\n{result}\n{closing_indent}}}"


def generate_diff(file_path1, file_path2):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)

    return build_diff(data1, data2)
