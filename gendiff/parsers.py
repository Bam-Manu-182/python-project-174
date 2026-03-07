import json
import yaml
import os


def parse(content, ext):
    if ext == '.json':
        return json.loads(content)
    elif ext in ['.yaml', '.yml']:
        return yaml.safe_load(content)
    raise ValueError(f"Unsupported format: {ext}")


def get_data(file_path):
    ext = os.path.splitext(file_path)[1]
    with open(file_path, 'r') as f:
        content = f.read()
    return parse(content, ext)
