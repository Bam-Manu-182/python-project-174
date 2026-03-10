from gendiff.formatters.stylish import render_stylish
from gendiff.formatters.plain import render_plain
from gendiff.formatters.json import render_json


def get_formatter(name):
    if name == 'plain':
        return render_plain

    if name == 'json':
        return render_json

    return render_stylish
