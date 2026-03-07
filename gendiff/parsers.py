import json
import yaml


def parse(content, ext):
    if ext == '.json':
        return json.loads(content)
    elif ext in ['.yaml', '.yml']:
        return yaml.safe_load(content)
    raise ValueError(f"Unsupported format: {ext}")
