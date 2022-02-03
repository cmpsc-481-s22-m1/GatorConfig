"""Capture user input to automatically generate YAML file."""
#from importlib.resources import path
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
@cli.command()
def cli_input(
    name: str = typer.Option(default_name(), help="The name of the project"),
    brk: bool = typer.Option(False, "--break", help="Enables break"),
    overwrite: bool = typer.Option(False, help="Allows GatorConfig to overwrite existing files"),
    fastfail: bool = typer.Option(False, help="Enables fastfail"),
    gen_readme: bool = typer.Option(False, help="Generates a README file"),
    file: List[str] = typer.Option([], help="""Enter singular file path, can be done
    multiple times"""),
    #language: str = typer.Option(None),
    output_path: Path = typer.Option(Path.cwd(), help="Enter preferred output path"),
    gui: bool = typer.Option(False, help="Open GatorConfig in GUI mode"),
    indent: int = typer.Option(4, help="Enter preferred indent"),
    commit_count: int = typer.Option(5, "--commits", help="Enter preferred minimum amount of commits")
):
    """Gather input from the command line.

    Args:
        name (str, optional): [description]. Defaults to typer.Option(default_name(), help="The name of the project").
        brk (bool, optional): [description]. Defaults to typer.Option(False, "--break", help="Enables break").
        overwrite (bool, optional): [description]. Defaults to typer.Option(False, help="Allows GatorConfig to overwrite existing files").
        fastfail (bool, optional): [description]. Defaults to typer.Option(False, help="Enables fastfail").
        gen_readme (bool, optional): [description]. Defaults to typer.Option(False, help="Generates a README file").
        file (List[str], optional): [description]. Defaults to typer.Option([], help="Enter singular file path, can be done multiple times").
        output_path (Path, optional): [description]. Defaults to typer.Option(Path.cwd(), help="Enter preferred output path").
        gui (bool, optional): [description]. Defaults to typer.Option(False, help="Open GatorConfig in GUI mode").
        indent (int, optional): [description]. Defaults to typer.Option(4, help="Enter preferred indent").
        commit_count (int, optional): [description]. Defaults to typer.Option(5, help="Enter preferred minimum amount of commits").
    """
    config_dir = output_path.joinpath("config")
    config_dir.mkdir(exist_ok=True)
    if overwrite or not config_dir.joinpath("gatorgrader.yml").exists():
        if gui:
            gui_obj = Gui()
            header, body = gui_obj.get_data()
        else:
            # Creation of the output variable
            body = get_checks(file)
            #print(files)
            # Creation of the output variable
            header = {
                "name": name,
                "break": brk,
                "fastfail": fastfail,
                "readme": gen_readme,
                "indent": indent,
                "commits": commit_count,
            }
        file_yaml = gatoryaml.dump(header, body)
        output_file(file_yaml, output_path)
    elif config_dir.joinpath("gatorgrader.yml").exists():
        print(f"\"gatorgrader.yml\" already exists within {config_dir}\n\nUse \"--overwrite\" to rewrite this file.")
    #print(files)
    actions_configuration.create_configuration_file('.github/workflows/grade.yml')


def output_file(yaml_string: str, output_path: Path):
    """Create and write to file if it doesn't exist, writes to file otherwise.

    Args:
        yaml_string (str): [description]
        output_path (Path): [description]
    """
    pth = Path(output_path / 'config')
    pth.mkdir(exist_ok=True)
    (pth / 'gatorgrader.yml').open('w').write(yaml_string)
    print(f"Wrote file to: {pth}" + "/gatorgrader.yml")

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
        print(f"These checks are added by default:\n {check_list}")
        print("")
        while running:
            check = input(f"Enter a check for {item} (Press \"Enter\" to move on): ")
            if check.lower() == "":
                running = False
            else:
                check_list.append(check)
        files[item] = list(set(check_list))
    return files

if __name__ == "__main__":
    cli()
