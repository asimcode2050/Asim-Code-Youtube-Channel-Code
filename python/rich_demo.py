from rich.console import Console
from rich.progress import Progress
import time
console = Console()
console.print("Hello","World!")
console.print("Hello","World!", style="bold red")
console.print("Hello world [bold cyan]test[/bold cyan] Hi [u]there[/u] , how [i]you[/i] ?")
console.print(":smiley: :vampire: :thumbs_up: :raccoon:")
with Progress() as progress:
    task1 = progress.add_task("[red]Downloading...",total=1000)
    task2 = progress.add_task("[green]Processing...",total=1000)

    while not progress.finished:
        progress.update(task1,advance=0.5)
        progress.update(task2,advance=0.3)
        time.sleep(0.02)