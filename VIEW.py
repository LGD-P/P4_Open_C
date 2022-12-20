
from rich.console import Console
from dataclasses import dataclass

c = Console()



@dataclass
class MenuView:
    menu: dict 

    def display_menu(self):
            c.print("\n[bold yellow]Bonjour, Veuillez faire un choix dans le menu:[bold yellow]\n")
            for element in self.menu:
                c.print(self.menu[element]["label"])
            choice = c.input("[bold red]==> [bold red]")
        

main_menu = MenuView({
    "1":{
        "label":"[bold blue]- 1. Créer un tournois\n  [bold blue]",
        "action":"",
            },
    "2":{
        "label":"[bold blue]- 2. Ajouter des joueurs\n  [bold blue]",
        "action":"",
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
        "action":"",
            }
    })













if __name__ == "__main__":
    main_menu.display_menu()