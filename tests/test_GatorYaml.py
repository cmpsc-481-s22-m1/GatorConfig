from src.GatorYaml import GatorYaml
import pytest

@pytest.mark.parametrize(
    "key,expected",
    [
        ("test", "test:\n"),
        ("key_1", "key_1:\n"),
        ("key2", "key2:\n"),
    ],
)

def test_output_key(key, expected):
    yaml = GatorYaml()
    yaml.output_key(key)
    assert yaml.output == expected

@pytest.mark.parametrize(
    "key,value,expected",
    [
        ("key", "value", False),
        ("(pure)", "good value", True),
        ("(pure)", "(pure) Code", True),
    ],
)

def test_is_keyword(key, value, expected):
    yaml = GatorYaml()
    assert yaml.is_keyword(key, value) == expected