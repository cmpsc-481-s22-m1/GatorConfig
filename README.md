# team4-GatorConfig

A simple Python project utilizing a CLI approach to automate generating configuration files for GatorGrader. The GitHub Actions workflow executes
[pytest](https://pytest.org/) (with
[coverage](https://pypi.org/project/pytest-cov/)) and
[pylint](https://pylint.org/) using the Poetry configuration, and checks
markdown with [markdownlint](https://github.com/DavidAnson/markdownlint) and
spelling with [cspell](https://cspell.org/).

## Requirements

- [Python](https://realpython.com/installing-python/)
- [Pipx](https://pypa.github.io/pipx/installation/)
- [Poetry](https://python-poetry.org/docs/#installing-with-pipx)

## Usage

### Installing Python dependencies

After cloning this project, you will likely want to instruct Poetry to create a
virtual environment and install the Python packages (like pytest and pylint)
listed in `pyproject.toml`.

To install Python dependencies:

```bash
poetry install
```

### Running tasks

This project uses the [taskipy](https://github.com/illBeRoy/taskipy) task runner
to simplify testing and linting. You can see the actual commands run when tasks
are executed under the `[tool.taskipy.tasks]` header in `pyproject.toml`.

- **Test** your code with `poetry run task test`
- **Lint** your code with `poetry run task lint`

### Running GatorConfig

GatorConfig is a tool that will utilize the command line interface, that was built to accommodate the users. To run the GatorConfig program in CLI, type the command:

`poetry run gatorconfig`

Once you run this command, the program will output

`Wrote file to: C:\Users\'YOUR PATH'\GatorConfig\gatorgrader.yml`

