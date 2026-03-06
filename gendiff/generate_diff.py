import json


def stringify(value):
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

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
