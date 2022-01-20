# import pytest
from typer.testing import CliRunner
from GatorConfig import GatorConfig
from .GatorConfig import cli

runner = CliRunner()

def test_cli_input():
    result = runner.invoke(cli, "--name", "Test", "--break", "--fastfail")
    assert result.exit_code == 0
    