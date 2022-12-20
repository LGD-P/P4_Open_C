import sys
from rich.console import Console
from dataclasses import dataclass


c = Console()


@dataclass
class MenuController:
    choice_from_menu : str
    
    def quit_menu(self):
        c.print("[bold red]Merci à bientôt[bold red]")
        sys.exit()
       
       
action_after_choice = MenuController("")

        
        
