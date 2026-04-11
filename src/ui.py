from rich.console import Console
from rich.panel import Panel

console = Console()

def titulo(texto):
    console.print(Panel(texto, style="bold magenta"))

def sucesso(msg):
    console.print(f"[bold magenta]✔ {msg}[/]")

def erro(msg):
    console.print(f"[red]✖ {msg}[/]")

def info(msg):
    console.print(msg)