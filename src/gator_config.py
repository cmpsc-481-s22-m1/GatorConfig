"""Capture user input to automatically generate YAML file."""
from typing import List
import typer
from src import actions_configuration

cli = typer.Typer()

#pylint: disable=too-many-arguments
@cli.command()
def cli_input(
    name: str = typer.Option("Project"),
    brk: bool = typer.Option(False, "--break"),
    fastfail: bool = typer.Option(False),
    file: List[str] = typer.Option([]),
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
    print(f"Name: {name}")
    print(f"Break: {brk}")
    print(f"Fastfail: {fastfail}")
    print(f"Files: {file}")
    print(f"Indent: {indent}")
    print(f"Commit Count: {commit_count}")

if __name__ == "__main__":
    cli()
    actions_configuration.create_configuration_file('../.github/workflows/grade.yml')
