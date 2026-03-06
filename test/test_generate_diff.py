from gendiff.generate_diff import generate_diff
import os


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "fixtures", file_name)


def test_generate_diff():
    path1 = get_fixture_path('file1.json')
    path2 = get_fixture_path('file2.json')

    expected = (
        "{\n"
        "- follow: false\n"
        "  host: hexlet.io\n"
        "- proxy: 123.234.53.22\n"
        "- timeout: 50\n"
        "+ timeout: 20\n"
        "+ verbose: true\n"
        "}"
    )

    assert generate_diff(path1, path2) == expected
