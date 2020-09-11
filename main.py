import typer
import requests

app = typer.Typer()

@app.command()
def get():
    r = requests.get('http://localhost:8080/bookmarks')
    bookmarks = r.json()
    for bookmark in bookmarks:
        typer.echo('----------')
        typer.echo(bookmark["name"])
        typer.echo(bookmark["url"])
        typer.echo('----------')

if __name__ == "__main__":
    app()
