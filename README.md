# GatorConfig

![logo](https://user-images.githubusercontent.com/42869122/152203388-39f5f0ef-e4c7-4f80-b667-07a4ed739b4d.png)

A simple Python project utilizing both a CLI and GUI approach
to automate the generation of configuration files for
[GatorGrader](https://github.com/GatorEducator/gatorgrader). The GitHub Actions
workflow executes [pytest](https://pytest.org/) (with
[coverage](https://pypi.org/project/pytest-cov/)) and
[pylint](https://pylint.org/) using the Poetry configuration, and checks
markdown with [markdownlint](https://github.com/DavidAnson/markdownlint) and
spelling with [cspell](https://cspell.org/).

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

`poetry run gatorconfig`

Once you run this command, the program will output:

`Wrote file to: C:\Users\<YOUR PATH>\config\gatorgrader.yml`

### GatorConfig CLI Tags

| Tag          | Description|
|--------------|-----------------------------------------------------------------------------------------|
| --name| Sets name for the project.  Defaults to name of current directory.|
| --break| Enables the `break` option in configuration file. Defaults to True.|
| --fastfail| Enables the `fastfail` option in configuration file.  Defaults to False.|
| --gen_readme | Creates markdown file with project name and instructions on running GatorGradle.|
| --file       | Specify path to file, can be used multiple times. No Default|
| --gui        | Opens GUI. **MUST HAVE ALL PACKAGES INSTALLED**|
| --indent     | Specify indent size.  Default is 4.|
| --commits    | Specify minimum commits a project must have. Default is 5|

This command will auto-generate a default configuration file for GatorGradle
named `gatorgrader.yml` located in the `config` folder.
This file will contain a default input for the variables,
such as the name, break, fastfail, etc.,

Additionally, you can run the `poetry run gatorconfig --help` for more
information about the configuration. This command will list the variables
in the file as well as the defaults it outputs.

## Contributing



### Running tasks

This project uses the [taskipy](https://github.com/illBeRoy/taskipy) task runner
to simplify testing and linting. You can see the actual commands run when tasks
are executed under the `[tool.taskipy.tasks]` header in `pyproject.toml`.

- **Test** your code with `poetry run task test`
- **Lint** your code with `poetry run task lint`