"""Capture user input to automatically generate YAML file."""
from typing import Dict
from typing import List
from pathlib import Path
import os
import typer
import gatoryaml
from gatorconfig.gui_main import Gui
from gatorconfig import actions_configuration

cli = typer.Typer()



def default_name():
    """Generate default name based on current directory."""
    return os.path.basename(Path.cwd())


#pylint: disable=too-many-arguments
#pylint: disable=too-many-locals
@cli.command()
def cli_input(
    name: str = typer.Option(default_name(), help="The name of the project"),
    no_break: bool = typer.Option(False, "--no-break", help="""Configure GatorGradle to not fail the
    grading run when a GatorGrader check fails"""),
    overwrite: bool = typer.Option(False, help="Allows GatorConfig to overwrite existing files"),
    fastfail: bool = typer.Option(False, help="""Configure GatorGradle to fail the grading run
    immediately when a single GatorGrader check fails"""),
    gen_readme: bool = typer.Option(False, help="Generates a README file"),
    file: List[str] = typer.Option([], help="""Enter singular file path, can be done
    multiple times"""),
    output_path: Path = typer.Option(Path.cwd(), help="Enter preferred output path"),
    indent: int = typer.Option(4, help="""Enter the number of spaces for an indentation
    level in the GatorGrader configuration file"""),
    actions: bool = typer.Option(True, help="Toggles whether or not github actions are created"),
    gui: bool = typer.Option(False, help="Open GatorConfig in GUI mode"),
):
    """Gather input from the command line."""
    config_dir = output_path / "config"
    config_path = config_dir / "gatorgrader.yml"
    config_dir.mkdir(exist_ok=True)
    if overwrite or not config_path.exists():
        if gui:
            gui_obj = Gui()
            header, body = gui_obj.get_data()
        else:
            # Creation of the output variable
            body = get_checks(file)
            # Creation of the output variable
            header = {
                "name": name,
                "break": not no_break,
                "fastfail": fastfail,
                "indent": indent,
            }
        file_yaml = gatoryaml.dump(header, body, indent=indent)
        output_file(file_yaml, config_path)
    elif config_path.exists():
        print(f"'gatorgrader.yml' already exists within {config_dir}")
        print("\nUse '--overwrite' to rewrite this file.")
    if actions:
        actions_configuration.create_configuration_file('.github/workflows/grade.yml')
    if gen_readme:
        readme_gen(output_path)


def readme_gen(output_path: Path):
    """Generate basic README in current directory."""
    if output_path.exists():
        with open(Path(output_path / "README.md"), "x", encoding="utf8") as file:
            file.write(
                "# " + default_name() + "\n" + "\n" +
                "This is the repository containing the " + default_name() + " assignment."
                + "\n" + "\n" + "## Using GatorGradle" + "\n" + "\n" +
                "This assignment utilizes " +
                "[GatorGrader](https://github.com/GatorEducator/gatorgrader)"
                " in order to perform automated grading checks." +
                " To grade your assignment, run the following command in your " +
                "Docker container or environment containing Gradle:"
                + "\n" + "\n" + "```" + "\n" + "gradle grade" + "\n" + "```" + "\n"
            )


def output_file(yaml_string: str, config_path: Path):
    """Create and write to file if it doesn't exist, writes to file otherwise.

    Args:
        yaml_string (str): [description]
        output_path (Path): [description]
    """
    config_path.parent.mkdir(exist_ok=True)
    config_path.open('w').write(yaml_string)
    print(f"Wrote file to: {config_path}")


def get_checks(file: List[Path]) -> Dict:
    """Read in checks per file.

    Args:
        file (List[Path]): List of file paths read in from command line.

    Returns:
        Dict: Dictionary of file paths and checks to perform per file.
    """
    files = {}
    for item in file:
        running = True
        check_list = ['--description "Confirm the file exists" ConfirmFileExists',
                      '--description "Make sure there are no TODOs in the file"'
                      ' MatchFileFragment --fragment "TODO" --count 0']
        print(f"These checks are added by default:\n {check_list} \n")
        while running:
            check = input(f"Enter a check for {item} (Press 'Enter' to move on to the next file): ")
            if check.lower() == "":
                running = False
            else:
                check_list.append(check)
        files[item] = check_list
    return files

if __name__ == "__main__":
    cli()
