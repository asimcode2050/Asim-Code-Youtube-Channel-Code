# https://www.youtube.com/watch?v=8C37ri_h-Q0&t=19s
import click
import glob

@click.command()
@click.option("--path",
    prompt="Path to search for files",  
    help="This is the path to search for files: /tmp",
)
@click.option(
    "--ftype",
     prompt="Please enter the file type",
        help="file type: txt",
)
def file_search(path,ftype):
    results = glob.glob(f"{path}/*.{ftype}")
    click.echo(click.style("Found Files:",fg="yellow"))
    for result in results:
        click.echo(click.style(f"{result}",bg="black",fg="green"))

if __name__=="__main__":
    file_search()

