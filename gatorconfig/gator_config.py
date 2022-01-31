"""Capture user input to automatically generate YAML file."""
from typing import Dict
from typing import List
from pathlib import Path
import typer
from gatorconfig import gator_yaml
from gatorconfig import actions_configuration

cli = typer.Typer()



#pylint: disable=too-many-arguments
@cli.command()
def cli_input(
    name: str = typer.Option("Project"),
    brk: bool = typer.Option(False, "--break"),
    fastfail: bool = typer.Option(False),
    gen_readme: bool = typer.Option(False),
    file: List[str] = typer.Option([]),
    #language: str = typer.Option(None),
    output_path: Path = typer.Option(Path.cwd()),
    indent: int = typer.Option(4),
    commit_count: int = typer.Option(5)
):
    """Gather input from the command line.

    Args:
        name (str, optional): [description]. Defaults to typer.Option("Project").
        brk (bool, optional): [description]. Defaults to typer.Option(False, "--break").
        fastfail (bool, optional): [description]. Defaults to typer.Option(False).
        file (List[str], optional): [description]. Defaults to typer.Option([]).
        indent (int, optional): [description]. Defaults to typer.Option(4).
        commit_count (int, optional): [description]. Defaults to typer.Option(5).
    """
    files = get_checks(file)

    yaml_out = gator_yaml.GatorYaml()
    #print(files)
    # Creation of the output variable
    output = {
        "name": name,
        "break": brk,
        "fastfail": fastfail,
        "readme": gen_readme,
        "indent": indent,
        "commits": commit_count,
        "files": files
    }
    file_yaml = yaml_out.dump(output, paths=output["files"])
    output_file(file_yaml, output_path)
    actions_configuration.create_configuration_file('.github/workflows/grade.yml')


def output_file(yaml_string: str, output_path: Path):
    """Create and write to file if it doesn't exist, writes to file otherwise.

    Args:
        yaml_string (str): [description]
        output_path (Path): [description]
    """
    fle = Path(output_path / "gatorgrader.yml")
    fle.touch(exist_ok=True)
    with open(fle, "w", encoding="utf8") as yml:
        yml.write(yaml_string)
    print(f"Wrote file to: {fle}")

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
        print("")
        check_list = ['--description "Confirm the file exists" ConfirmFileExists',
                      '--description "Make sure there are no TODOs in the file"'
                      ' MatchFileFragment --fragment "TODO" --count 0']
        while running:
            check = input(f"Enter a check for {item} (Press \"Enter\" to move on): ")
            if check.lower() == "":
                running = False
            else:
                check_list.append(check)
        files[item] = set(check_list)
    return files

if __name__ == "__main__":
    cli()
