from rich.console import Console
from dataclasses import dataclass

from CONTROLLER import *

c = Console()

STARTING_MENU = True

@dataclass
class MenuView:
    menu: dict 
    
    def display_menu(self):
        c.print("\n[bold yellow]Bonjour, Veuillez faire un choix dans "\
            "le menu:[bold yellow]\n")
        for element in self.menu:
            c.print(self.menu[element]["label"])
        menu_choice = c.input("[bold red]==> [bold red]")
        return menu_choice
        
    def display_choices(self,choice):
        if choice in MAIN_MENU.menu:
            MAIN_MENU.menu[choice]["action"]()

                
        
MAIN_MENU = MenuView({
    "1":{
        "label":"[bold blue]- 1. Créer un tournois\n  [bold blue]",
        "action":action_after_choice.creat_tournament,
            },
    "2":{
        "label":"[bold blue]- 2. Ajouter des joueurs\n  [bold blue]",
        "action":action_after_choice.add_player,
            },
    "3":{
        "label":"[bold blue]- 3. Lancer un tournois\n  [bold blue]",
            "action":"",
            },
    "4":{
        "label":"[bold blue]- 4. Ajouter des résultats\n  [bold blue]",
        "action":"",
            },
    "5":{
        "label":"[bold blue]- 5. Montrer le rapport\n  [bold blue]",
        "action":"",
            },
    "6":{
        "label":"[bold blue]- 6. Quitter\n  [bold blue]",
        "action":action_after_choice.quit_menu
            }
    })




if __name__ == "__main__":
    while STARTING_MENU:
        user_choices = MAIN_MENU.display_menu()
        MAIN_MENU.display_choices(user_choices)

    