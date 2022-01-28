"""Test functions within gator_config"""
import pytest
from typer.testing import CliRunner
from src.gator_config import output_file
from src.gator_config import cli

runner = CliRunner()
# @pytest.mark.skip(reason="no way of currently testing this")
@pytest.fixture()
def test_cli_input(mocker, tmpdir):
    """Test cli input with every flag"""
    test_dir = tmpdir.mkdir("testing")
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
        6,
        "--output-path",
        test_dir
        ])
    assert "Wrote file to: " in result.stdout()
    print("Test Output:", result.stdout())
    test_file = test_dir.joinpath("gatorgrader.yml")
    with mocker.patch('builtins.input', return_value=""):
        assert test_file.exists()
    with open(test_file, encoding='utf-8') as fle:
        #print(fle.read())
        assert "name: Test" in fle.read()

@pytest.fixture()
def test_cli_no_input(mocker, tmpdir):
    """Test cli input with no flags"""
    test_dir = tmpdir.mkdir("testing")
    result = runner.invoke(cli)
    assert "Wrote file to: " in result.stdout()
    test_file = test_dir.joinpath("gatorgrader.yml")
    with mocker.patch('builtins.input', return_value=""):
        assert test_file.exists()
    with open(test_file, encoding='utf-8') as fle:
        #print(fle.read())
        assert "name: Project" in fle.read()


@pytest.mark.parametrize("input_text", ["I am text"])

@pytest.fixture()
def test_output_file(tmpdir, input_text):
    test_dir = tmpdir.mkdir("testing")
    test_file_path = test_dir.joinpath("gatorgrader.yml")    
    assert test_file_path.exists() == False
    output_file(input_text, test_dir)
    assert test_file_path.exists()
    assert "I am text" in test_file_path
