"""Test functions within gator_config"""
import pytest
from pytest_mock import MockerFixture
from typer.testing import CliRunner
from gatorconfig.gator_config import cli
from gatorconfig.gator_config import output_file

runner = CliRunner()
# @pytest.mark.skip(reason="no way of currently testing this")
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
    #print("Test Output:", result.stdout())
    test_file = test_dir / "gatorgrader.yml"
    with mocker.patch('builtins.input', return_value=""):
        assert test_file.exists()
    with open(test_file, encoding='utf-8') as fle:
        #print(fle.read())
        assert "name: Test" in fle.read()

def test_cli_no_input(mocker: MockerFixture, tmpdir: MockerFixture):
    """Test cli input with no flags"""
    test_dir = tmpdir.mkdir("testing")
    result = runner.invoke(cli, ["--output-path", test_dir])
    test_file = test_dir / "gatorgrader.yml"
    with mocker.patch('builtins.input', return_value=""):
        assert test_file.exists()
    with open(test_file, encoding='utf-8') as fle:
        #print(fle.read())
        assert "name: Project" in fle.read()


#@pytest.mark.parametrize("input_text", ["I am text"])

def test_output_file(tmpdir):
    """Test creation of file, and if the file has the correct contents"""
    input_text = "I am text"
    test_dir = tmpdir.mkdir("testing")
    test_file_path = test_dir / "gatorgrader.yml"
    assert test_file_path.exists() is False
    output_file(input_text, test_dir)
    assert test_file_path.exists()
    with open(test_file_path) as test_file:
        assert "I am text" in test_file.read()
