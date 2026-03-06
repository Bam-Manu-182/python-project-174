import json
import yaml


def stringify(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def load_data(file_path):
    if file_path.endswith('.json'):
        return json.load(open(file_path))
    elif file_path.endswith(('.yaml', '.yml')):
        return yaml.safe_load(open(file_path))


def generate_diff(file_path1, file_path2):
    data1 = load_data(file_path1)
    data2 = load_data(file_path2)

    keys = sorted(set(data1.keys()) | set(data2.keys()))

    result = "{\n"
    for key in keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                result += f"  {key}: {stringify(data1[key])}\n"
            else:
                result += f"- {key}: {stringify(data1[key])}\n"
                result += f"+ {key}: {stringify(data2[key])}\n"
        elif key in data1:
            result += f"- {key}: {stringify(data1[key])}\n"
        else:
            result += f"+ {key}: {stringify(data2[key])}\n"
    result += "}"
    return result

