from rich.console import Console
from dataclasses import dataclass

from CONTROLLER_V2 import *

c = Console()

STARTING_MENU = True

@dataclass
class MenuView:
    menu_view: dict 
    menu_choice : str = None
    
    def display_menu(self):
        c.print("\n[bold yellow] :clipboard: CHESS MENU Veuillez faire un choix "\
            "dans le menu: :clipboard: [bold yellow]\n")
        for element in self.menu_view:
            c.print(self.menu_view[element]["label"])
        self.menu_choice = c.input("[bold red]==> [bold red]")
        return self.menu_choice
        
    def display_choices(self):
        if self.menu_choice in MAIN_MENU.menu_view:
            MAIN_MENU.menu_view[self.menu_choice]["action"]()
        else:
            c.print("\n[bold red]Merci de faire un choix présent"\
                    " dans le menu[bold red]\n")
              
        

@dataclass
class TournamentView:
    tournament_view : dict
    tournament_choice : str = None
      
    def display_tournemanent_menu(self):
        c.print("\n[bold yellow]Possibilité en rapport avec les tournois "\
            "[bold yellow]\n")
        for element in self.tournament_view:
            c.print(self.tournament_view[element]["label"])
        self.tournament_choice = c.input("[bold red]==> [bold red]")
        return self.tournament_choice
        
    def display_tournament_choices(self):
        if self.tournament_choice in TOURNAMENT_MENU_VIEW.tournament_view:
            TOURNAMENT_MENU_VIEW.tournament_view[self.tournament_choice]["action"]()

   
   
    
TOURNAMENT_MENU_VIEW = TournamentView(
    {"1":{
        "label":"[bold blue]- 1. Afficher les tournois [bold blue]",
        "action": action_in_tournmanent_menu.display_tournament_list    
         },
     "2":{"label":"[bold blue]- 2. Ajouter un tournois [bold blue]\n",
          "action": action_in_tournmanent_menu.add_tournament
    }
    })



MAIN_MENU = MenuView({
    "1":{
        "label":"[bold blue]- 1. Gérer des tournois :pencil: [bold blue]",
        "action":TOURNAMENT_MENU_VIEW.display_tournemanent_menu,
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
        "action": action_to_quit.quit_menu
            }
    })





if __name__ == "__main__":
    while STARTING_MENU:
        MAIN_MENU.display_menu()
        MAIN_MENU.display_choices()   
        TOURNAMENT_MENU_VIEW.display_tournament_choices()
   

          