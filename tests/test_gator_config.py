"""Test functions within gator_config"""
import pathlib
import pytest
import mock
from typer.testing import CliRunner
from src.gator_config import cli

runner = CliRunner()

@pytest.mark.skip(reason="no way of currently testing this")
def test_cli_input():
    """Test cli input with every flag"""
    # pylint: disable=W0612
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
        assert result.exit_code == 0
        assert output.exists()
    with open(output, encoding='utf-8') as fle:
        assert "name: Project" in fle.read()

@pytest.mark.parametrize("expected",[""])

# pylint: disable=W0613
def test_cli_no_input(expected):
    """Test cli input with no flags"""
    # pylint: disable=W0612
    result = runner.invoke(cli)
    output = pathlib.Path.cwd().joinpath("gatorgrader.yml")
    with mock.patch('builtins.input', return_value="stop"):
        assert output.exists()
    with open(output, encoding='utf-8') as fle:
        assert "name: Project" in fle.read()


# pytest.mark.parametrize()

# def test_output_file():
#     pass
