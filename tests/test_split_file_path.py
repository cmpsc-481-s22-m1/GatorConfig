"""Test split_file_path function."""

import pytest
from src.split_file_path import split_file_path


def test_output_as_dic():
    """Ensure output is a dictionary."""
    input_dic = {"sample/file.py": ['']}
    output = split_file_path(input_dic)
    assert isinstance(output, dict)

@pytest.mark.parametrize(
    "test_input,expected",
    [({'src/main/java/samplelab/SampleLabMain.java': [''],
    'src/main/java/samplelab/DataClass.java': ['']},
    {'src': {'main': {'java': {'samplelab':
    {'SampleLabMain.java': [''], 'DataClass.java': ['']}}}}}),
    ({'src/main/java/samplelab/SampleLabMain.java': [''],
    'writing/reflection.md': ['']}, {'src': {'main': {'java': {'samplelab':
    {'SampleLabMain.java': ['']}}}}, 'writing': {'reflection.md': ['']}}),
    ({'src/main/java/samplelab/DataClass.java': [''],
    'src/main/java/HelloWorld.java': ['']},
    {'src': {'main': {'java': {'samplelab': {'DataClass.java': ['']},
    'HelloWorld.java': ['']}}}})
    ]
)

def test_dic_nesting(test_input, expected):
    """Ensure directories are nested correctly."""
    output = split_file_path(test_input)
    assert output == expected
