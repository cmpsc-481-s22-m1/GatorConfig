"""Capture user input to automatically generate YAML file."""
import gator_yaml
from typing import List
import typer

cli = typer.Typer()



#pylint: disable=too-many-arguments
@cli.command()
def cli_input(
    name: str = typer.Option("Project"),
    brk: bool = typer.Option(False, "--break"),
    fastfail: bool = typer.Option(False),
    gen_readme: bool = typer.Option(False),
    file: List[str] = typer.Option([]),
    check: List[str] = typer.Option([]),
    #language: str = typer.Option(None),
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
    yaml_out = gator_yaml.GatorYaml()
    files = dict(zip(file, check))
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
    print(f"Files: {output['files']}")
    file_yaml = yaml_out.dump(output)
    print(f"Yaml:\n{file_yaml}")

if __name__ == "__main__":
    cli()
