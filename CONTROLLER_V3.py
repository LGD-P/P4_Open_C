from rich.console import Console
import sys

from MODEL_V3 import Tournament, Players
from VIEW_V3 import MenuView

c = Console  
        
class MenuController:
    def __init__(self):
        self.running_program = True
        self.menu_view_in_controller = MenuView({
    "1":{
        "label":"[bold blue]- 1. Gérer des tournois :pencil: [bold blue]",
        "action":"",
            },
    "2":{
        "label":"[bold blue]- 2. Gérer des joueurs :pencil: [bold blue]",
        "action":"",
            },
    "3":{
        "label":"[bold blue]- 3. Lancer un tournois :watch:[bold blue]",
            "action":"",
            },
    "4":{
        "label":"[bold blue]- 4. Ajouter des résultats :trophy: [bold blue]",
        "action":"",
            },
    "5":{
        "label":"[bold blue]- 5. Montrer le rapport :bar_chart: [bold blue]",
        "action":"",
            },
    "6":{
        "label":"[bold blue]- 6. Quitter :raising_hand: \n [bold blue]",
        "action": MenuController.quit_menu
            }
    })


    def quit_menu(self):
        c.print("[bold red]Merci à bientôt[bold red]")
        sys.exit() 
        
    def run_program(self):
        while self.running_program:
            self.menu_view_in_controller.display_menu()
            self.menu_view_in_controller.display_choices()
        

