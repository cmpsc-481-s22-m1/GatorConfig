import yaml

build_file = open('.github/workflows/gatorgradle.yml', 'w')

yaml.dump({'name': 'GatorGradle', 'on': ['push', 'pull_request'], 'jobs':
    {'grade': {'runs-on': 'ubuntu-latest', 'steps': [
        {'name': 'Checkout repository', 'uses': 'actions/checkout@v2'},
        {'name': 'Setup Python 3.9', 'uses': 'actions/setup-python@v2', 'id': 'setup-python', 'with': {'python-version': '3.9'}},
        {'name': 'Check for existence of gradle files', 'uses': 'andstor/file-existence-action@v1', 'with': {'files': 'build.gradle, gradle.properties, settings.gradle, gatorgrader.yml'}},
        {'name': 'Determine gradle version', 'run': 'gradle --version'},
        {'name': 'Run GatorGrader', 'run': 'gradle grade'}]}}}, build_file)
