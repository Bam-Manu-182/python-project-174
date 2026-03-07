import os
from gendiff.parsers import parse


def stringify(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def get_data(file_path):
    _, ext = os.path.splitext(file_path)
    with open(file_path, 'r') as f:
        content = f.read()
    return parse(content, ext)


def generate_diff(file_path1, file_path2):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))

    result = "{\n"
    for key in keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                result += f"   {key}: {stringify(data1[key])}\n"
            else:
                result += f"  - {key}: {stringify(data1[key])}\n"
                result += f"  + {key}: {stringify(data2[key])}\n"
        elif key in data1:
            result += f"  - {key}: {stringify(data1[key])}\n"
        else:
            result += f"  + {key}: {stringify(data2[key])}\n"
    result += "}"
    return result
