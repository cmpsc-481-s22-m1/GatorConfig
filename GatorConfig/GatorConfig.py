import typer
from typing import List

cli = typer.Typer()

@cli.command()
def cli_input(
    name: str = typer.Option("Project"),
    brk: bool = typer.Option(False, "--break"),
    fastfail: bool = typer.Option(False),
    file: List[str] = typer.Option([]),
    indent: int = typer.Option(4),
    commit_count: int = typer.Option(5)
):
    print(f"Name: {name}\nBreak: {brk}\nFastfail: {fastfail}\nFiles: {file}\nIndent: {indent}\nCommit Count: {commit_count}\n")

if __name__ == "__main__":
    cli()