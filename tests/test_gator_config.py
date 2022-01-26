"""Test functions within gator_config"""
import pytest
import mock
import pathlib
from typer.testing import CliRunner
from src.gator_config import cli

runner = CliRunner()

def test_cli_input():
    """Test cli input with every flag"""
    result = runner.invoke(cli, [
        "--name",
        "Test",
        "--break",
        "--fastfail",
        "--file",
        "Object 1",
        "--indent",
        6,
        "--commit-count",
        6
        ])
    output = pathlib.Path.cwd().joinpath("gatorgrader.yml")
    with mock.patch('builtins.input', return_value="stop"):
        assert output.exists()
    with open(output) as fle:
        assert "name: Project" in fle.read()

@pytest.mark.parametrize("expected",[""])

def test_cli_no_input(expected):
    """Test cli input with no flags"""
    result = runner.invoke(cli)
    output = pathlib.Path.cwd().joinpath("gatorgrader.yml")
    with mock.patch('builtins.input', return_value="stop"):
        assert output.exists()
    with open(output) as fle:
        assert "name: Project" in fle.read()


# pytest.mark.parametrize()

# def test_output_file():
#     pass
