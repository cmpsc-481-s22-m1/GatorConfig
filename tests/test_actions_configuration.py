"""This module tests the githubactions.create_actions_configuration module"""
import src.actions_configuration

def test_create_configuration_file(tmpdir):
    """Check that the configuration file is actually created"""
    path = tmpdir.mkdir('sub').join('config.yml')
    src.actions_configuration.create_configuration_file(path)
    assert path.read() == """name: Grade
on:
- push
- pull_request
jobs:
  grade:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repository
      uses: actions/checkout@v2
    - name: Run GatorGradle
      uses: GatorEducator/gatorgradle-action@v1
"""
    assert len(tmpdir.listdir()) == 1
