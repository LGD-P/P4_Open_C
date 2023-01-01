from rich.console import Console
from datetime import datetime

from MODEL_V3 import Players, Tournament

c = Console()

class MenuView:
    def __init__(self, menu_view ):
        self.menu_view = menu_view

    
    def display_menu_and_get_choice(self):
        c.print("\n[bold yellow] :clipboard: CHESS MENU Veuillez faire un choix "\
            "dans le menu: :clipboard: [bold yellow]\n")
        for element in self.menu_view:
            c.print(self.menu_view[element]["label"])
        menu_choice = c.input("[bold red]==> [bold red]")

        if menu_choice in self.menu_view:
            return self.menu_view[menu_choice]["action"]()
        c.print("\n[bold red]Merci de faire un choix présent"\
                " dans le menu[bold red]\n")
    
    

   

class PlayerView:
    def __init__(self, players_list_view=[]):
        self.players_list_view = players_list_view
    
    def display_players_to_choose(self):
        counter = -1
        value = []
        key = [] 
        if self.players_list_view :
            c.print("[bold yellow] Liste des joueurs disponibles:\n[bold yellow]")
            
            for players in self.players_list_view :
                value.append(f"{players.last_name}  {players.first_name}  classement = {players.rank}")
        
            for _ in range(len(value)):
                counter += 1
                key.append(counter)
        
            players_availables = dict(zip(key,value))
            
            for k,v in players_availables.items():
                c.print(f"[bold blue]- {k}: {v}[bold blue]\n")
                
            return players_availables
        else:
            c.print("[bold red]Aucun joueurs n'a été créé...[bold red]")


class TournamentView:
    def __init__(self, tournament_list_view = []):
        self.tournament_list_view = tournament_list_view

    def display_tournament(self):
        counter = -1
        value = []
        key = [] 
        if self.tournament_list_view:
            c.print("[bold yellow] Tournois disponibles : \n[bold yellow]")
            for tournament in self.tournament_list_view:
                value.append(f"{tournament.name},{tournament.place}")
            for _ in range(len(value)):
                counter +=1
                key.append(counter)
                
            tournaments_availables = dict(zip(key,value))
            
            for k,v in tournaments_availables.items():
                c.print(f"[bold bleu]- {k} : {v}[bold bleu]")
                
            return tournaments_availables
    





if __name__ == "__main__":
    TournamentView().display_tournament()