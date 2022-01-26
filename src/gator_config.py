"""Capture user input to automatically generate YAML file."""
from typing import List
from pathlib import Path
import typer
import gator_yaml

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


def output_file(yaml_string, output_path: Path):
    fle = output_path.joinpath("gatorgrader.yml")
    fle.touch(exist_ok=True)
    with open(fle, "w") as f:
        f.write(yaml_string)
    print(f"Wrote file to: {fle}")

def get_checks(file):
    files = {}
    for item in file:
        running = True
        print("")
        check_list = []
        while running:
            check = typer.prompt(f"Enter a check for {item} (type \"stop\" to move on)")
            if check.lower() == "stop":
                running = False
            else:
                check_list.append(check)
        files[item] = check_list
    return files

if __name__ == "__main__":
    cli()
