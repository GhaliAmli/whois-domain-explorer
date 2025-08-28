import whois
import requests
import re
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def fetch_whois(domain):
    try:
        w = whois.whois(domain)
        table = Table(title=f"WHOIS Data for {domain}", show_lines=True)
        table.add_column("Field", style="cyan", no_wrap=True)
        table.add_column("Value", style="magenta")

        for key, value in w.items():
            if value:
                table.add_row(str(key), str(value))
        console.print(table)
    except Exception as e:
        console.print(f"[bold red]Error fetching WHOIS:[/bold red] {e}")

def fetch_ip_info(ip):
    try:
        res = requests.get(f"https://ipinfo.io/{ip}/json")
        data = res.json()
        table = Table(title=f"IP Info for {ip}", show_lines=True)
        table.add_column("Field", style="cyan")
        table.add_column("Value", style="magenta")
        for key, value in data.items():
            table.add_row(str(key), str(value))
        console.print(table)
    except Exception as e:
        console.print(f"[bold red]Error fetching IP info:[/bold red] {e}")

def is_ip(address):
    return re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", address)

def main():
    console.print(Panel("[bold green]Welcome to the Domain & IP Explorer[/bold green]", expand=False))
    target = console.input("[bold yellow]Enter a domain or IP:[/bold yellow] ").strip()
    
    if is_ip(target):
        fetch_ip_info(target)
    else:
        fetch_whois(target)

if __name__ == "__main__":
    main()