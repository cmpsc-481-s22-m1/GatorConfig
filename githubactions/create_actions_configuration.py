import ruamel.yaml as yaml

build_file = open('../.github/workflows/grade.yml', 'w')

yaml_str = """\
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

data = yaml.round_trip_load(yaml_str)
yaml.round_trip_dump(data, build_file, indent=4)