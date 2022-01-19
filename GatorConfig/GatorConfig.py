import typer

cli = typer.Typer()

@cli.command()
def main(
    placeholder1: bool = typer.Option(False),
    placeholder2: int = typer.Option(10)
):
    typer.echo(f"Placeholder 1: {placeholder1}\nPlaceholder 2: {placeholder2}")

if __name__ == "__main__":
    cli()