from gendiff.formatters.stylish import render_stylish
from gendiff.formatters.plain import render_plain


def get_formatter(name):
    if name == 'plain':
        return render_plain
    return render_stylish
