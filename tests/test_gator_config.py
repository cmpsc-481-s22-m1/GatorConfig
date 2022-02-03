"""Test functions within gator_config"""
#from pathlib import Path
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
    with mocker.patch('builtins.input', return_value=""):
        result = runner.invoke(cli, [
            "--name",
            "Test",
            "--break",
            "--fastfail",
            "--file",
            "Object 1",
            "--indent",
            6,
            "--commits",
            6,
            "--output-path",
            test_dir
            ])
    print("Test Output:", result.stdout)
    test_file = test_dir / "config" / "gatorgrader.yml"
    with mocker.patch('builtins.input', return_value=""):
        assert test_file.exists()
    with open(test_file, encoding='utf-8') as fle:
        print(fle.read())

def test_cli_no_input(mocker: MockerFixture, tmpdir):
    """Test cli input with no flags"""
    test_dir = tmpdir.mkdir("testing")
    result = runner.invoke(cli, ["--output-path", test_dir])
    assert result.exit_code == 0
    test_file = test_dir / "config" / "gatorgrader.yml"
    with mocker.patch('builtins.input', return_value=""):
        assert test_file.exists()
    with open(test_file, encoding='utf-8') as fle:
        #print(fle.read())
        assert "name: GatorConfig" in fle.read()

def test_cli_overwrite(tmpdir):
    """Test cli \"--overwrite\" flag"""
    test_dir = tmpdir.mkdir("testing")
    test_file = test_dir / "config" / "gatorgrader.yml"
    result = runner.invoke(cli, ["--output-path", test_dir, "--overwrite"])
    assert result.exit_code == 0
    with open(test_file, encoding="utf8") as fle:
        assert "break: True" in fle.read()
#@pytest.mark.parametrize("input_text", ["I am text"])

def test_output_file(tmpdir):
    """Test creation of file, and if the file has the correct contents"""
    input_text = "I am text"
    test_dir = tmpdir.mkdir("testing")
    test_file = test_dir / "config" / "gatorgrader.yml"
    assert test_file.exists() is False
    output_file(input_text, test_dir)
    assert test_file.exists()
    with open(test_file, encoding='utf-8') as test_file:
        assert "I am text" in test_file.read()
