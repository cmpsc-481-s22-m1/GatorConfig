"""This module generates a GitHub Actions configuration file that uses GatorGradle"""
from ruamel import yaml

def create_configuration_file(target_file):
    """Create the workflow configuration file itself"""
    str = """\
    name: Grade
    on: [push, pull_request]
    jobs:
      grade:
        runs-on: ubuntu-latest
        steps:
          - name: Checkout repository
            uses: actions/checkout@v2
          - name: Run GatorGradle
            uses: GatorEducator/gatorgradle-action@v1
    """
    data = yaml.round_trip_load(str)

    with open(target_file, 'w', encoding='utf-8') as build_file:
        yaml.round_trip_dump(data, build_file, indent=2)

if __name__ == "__main__":
    create_configuration_file('../.github/workflows/grade.yml')
