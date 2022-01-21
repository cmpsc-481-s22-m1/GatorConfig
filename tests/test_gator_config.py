"""Test functions within gator_config"""
# import pytest
from typer.testing import CliRunner
from GatorConfig.gator_config import cli

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
        "--file",
        "Object 2",
        "--indent",
        6,
        "--commit-count",
        6
        ])
    assert result.exit_code == 0
    assert "Name: Test" in result.stdout
    assert "Break: True" in result.stdout
    assert "Fastfail: True" in result.stdout
    assert "Files: (\'Object 1\', \'Object 2\')" in result.stdout
    assert "Indent: 6" in result.stdout
    assert "Commit Count: 6" in result.stdout

def test_cli_no_input():
    """Test cli input with no flags"""
    result = runner.invoke(cli)
    assert result.exit_code == 0    
    assert "Name: Project" in result.stdout
    assert "Break: False" in result.stdout
    assert "Fastfail: False" in result.stdout
    assert "Files: ()" in result.stdout
    assert "Indent: 4" in result.stdout
    assert "Commit Count: 5" in result.stdout
