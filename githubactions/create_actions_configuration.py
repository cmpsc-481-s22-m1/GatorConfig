"""This module generates a GitHub Actions configuration file that uses GatorGradle"""
from ruamel import yaml

YAML_STR = """\
name: Grade
on: [push]
jobs:
  grade:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
      - name: Run GatorGradle
        uses: GatorEducator/gatorgradle-action@v1
"""
data = yaml.round_trip_load(YAML_STR)

with open('../.github/workflows/grade.yml', 'w', encoding='utf-8') as build_file:
    yaml.round_trip_dump(data, build_file, indent=2)
