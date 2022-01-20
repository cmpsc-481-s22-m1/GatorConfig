import typer
from typing import List

cli = typer.Typer()

@cli.command()
def main(
    name: str = typer.Option("Project"),
    brk: bool = typer.Option(False, "--break"),
    fastfail: bool = typer.Option(False),
    files: List[str] = typer.Option([]),
    indent: int = typer.Option(4),
    commit_count: int = typer.Option(5)
):
    typer.echo(f"Name: {name}\nBreak: {brk}\nFastfail: {fastfail}\nFiles: {files}\nIndent: {indent}\nCommit Count: {commit_count}\n")

if __name__ == "__main__":
    cli()