from rich.console import Console
from datetime import datetime
import sys


from VIEW.menu_view import MenuView
from VIEW.tournament_view import TournamentView
from VIEW.player_view import PlayerView

from CONTROLLER.player_controller import PlayerController
from CONTROLLER.tournament_controller import TournamentController


c = Console()  



        
class MenuController:
    def __init__(self):
        self.player_controller = PlayerController([])
        self.tournament_controller = TournamentController([],self.player_controller.player_list)
        self.menu_view_in_controller = MenuView({
    "1":{
        "label":"[bold blue]- 1. Créer des tournois :pencil: [bold blue]",
        "action":self.tournament_controller.add_tournament,
            },
    "2":{
        "label":"[bold blue]- 2. Créer des joueurs :pencil: [bold blue]",
        "action":self.player_controller.add_player,
            },
    "3":{
        "label":"[bold blue]- 3. Ajouter des joueurs à un tournois :pencil:[bold blue]",
            "action":self.tournament_controller.add_player_in_tournament,
            },
    "4":{
        "label":"[bold blue]- 4. Lancer un tournois :watch:[bold blue]",
            "action":"",
            },
    "5":{
        "label":"[bold blue]- 5. Ajouter des résultats :trophy: [bold blue]",
        "action":"",
            },
    "6":{
        "label":"[bold blue]- 6. Montrer le rapport :bar_chart: [bold blue]",
        "action":"",
            },
    "7":{
        "label":"[bold blue]- 7. Quitter :raising_hand: \n [bold blue]",
        "action": self.quit_menu
            }
    })


    def run_program(self, running_program=True):
        while running_program:
            self.menu_view_in_controller.display_menu_and_get_choice()
            
    def quit_menu(self):
        c.print("[bold red]Merci à bientôt[bold red]")
        sys.exit() 