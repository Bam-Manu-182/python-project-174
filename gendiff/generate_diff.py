from gendiff.parsers import get_data
from gendiff.formatters import get_formatter


def build_diff(data1, data2):
    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []
    for key in keys:
        val1 = data1.get(key)
        val2 = data2.get(key)

        if key not in data1:
            diff.append({'key': key, 'type': 'added', 'value': val2})

        elif key not in data2:
            diff.append({'key': key, 'type': 'removed', 'value': val1})

        elif data1[key] != data2[key]:
            diff.append({
                'key': key,
                'type': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            })

        elif val1 == val2:
            diff.append({'key': key, 'type': 'unchanged', 'value': val1})

        else:
            diff.append({
                'key': key,
                'type': 'changed',
                'old_value': val1, 'new_value': val2
            })

    return diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)

    diff_tree = build_diff(data1, data2)
    format_function = get_formatter(format_name)

    return format_function(diff_tree)
