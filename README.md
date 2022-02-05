# GatorConfig

![logo](https://user-images.githubusercontent.com/42869122/152203388-39f5f0ef-e4c7-4f80-b667-07a4ed739b4d.png)

A simple Python tool utilizing both a CLI and GUI approach
to automate the generation of configuration files for
[GatorGrader](https://github.com/GatorEducator/gatorgrader).
This tool is designed to assist educators in grading
GitHub-based assignments for their computer science courses.

## Requirements

- [Python](https://realpython.com/installing-python/)
- [Pipx](https://pypa.github.io/pipx/installation/)
- [Poetry](https://python-poetry.org/docs/#installing-with-pipx)

## Usage

### Install with pip or pipx

To install the tool and its dependencies using pip, run the following command:

```bash
pip install gatorconfig
```

Alternatively, you can install using pipx by running:

```bash
pipx install gatorconfig
```

### Running GatorConfig

GatorConfig is a tool that can utilize the command line interface, which
was built to accommodate the users. To run the GatorConfig program
in CLI, type the command:

`gatorconfig`

Once you run this command, the program will output:

`Wrote file to: C:\Users\<YOUR PATH>\config\gatorgrader.yml`

This command will auto-generate a default configuration file for GatorGradle
named `gatorgrader.yml` located in the `config` folder.

Additionally, you can run the `gatorconfig --help` for more
information about the configuration. This command will list the variables
in the file as well as the defaults it outputs.

## Contributing

### Technical details

The GitHub Actions
workflow executes [pytest](https://pytest.org/) (with
[coverage](https://pypi.org/project/pytest-cov/)) and
[pylint](https://pylint.org/) using the Poetry configuration, and checks
markdown with [markdownlint](https://github.com/DavidAnson/markdownlint) and
spelling with [cspell](https://cspell.org/).

### Installing Python dependencies

After cloning this project, you will likely want to instruct Poetry to create a
virtual environment and install the Python packages (such as pytest and pylint)
listed in `pyproject.toml`.

To install Python dependencies:

```bash
poetry install -E gui
```

To install without the extra GUI feature, install with:

```bash
poetry install
```

### Running tasks

This project uses the [taskipy](https://github.com/illBeRoy/taskipy) task runner
to simplify testing and linting. You can see the actual commands run when tasks
are executed under the `[tool.taskipy.tasks]` header in `pyproject.toml`.

- **Test** your code with `poetry run task test`
- **Lint** your code with `poetry run task lint`

## Authors

- Wesley Long, @WesleyL30 - *Lead CLI developer*
- Danny Ullrich, @ullrichd21 - *Lead GUI developer*
- Kobe Coleman, @ColemanKobe
- Paige Downey, @PaigeCD
- Favour Ojo, @favourojo
