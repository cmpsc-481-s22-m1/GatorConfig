import yaml

build_file = open('../.github/workflows/grade.yml', 'w')
yaml.dump({'name': 'Grade', True: ['push'], 'jobs': {'grade': {'runs-on': 'ubuntu-latest', 'steps': [{'name': 'Checkout repository', 'uses': 'actions/checkout@v2'}, {'name': 'Run GatorGradle', 'uses': 'GatorEducator/gatorgradle-action@v1'}]}}}, build_file)