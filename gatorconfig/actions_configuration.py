"""This module generates a GitHub Actions configuration file that uses GatorGradle"""
from pathlib import Path
from ruamel.yaml import YAML

def create_configuration_file(target_file):
    """Create the workflow configuration file itself"""
    default = {'name': 'Grade', 'on': ['push', 'pull_request'], 'jobs':
        {'grade': {'runs-on': 'ubuntu-latest', 'steps':
            [{'name': 'Checkout repository', 'uses': 'actions/checkout@v2'},
             {'name': 'Run GatorGradle', 'uses': 'GatorEducator/gatorgradle-action@v1'}]}}}
    yaml = YAML()
    yaml.default_flow_style = False
    out = Path(target_file)
    yaml.dump(default, out)
