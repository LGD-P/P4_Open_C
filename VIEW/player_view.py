from rich.console import Console
from datetime import datetime

from MODEL.tournament_model import Tournament
from MODEL.player_model import Player

c = Console()


class PlayerView:

    
    def display_players_to_choose(self, player_list, tourament_list):
        counter = -1
        value = []
        key = [] 
        if player_list :                                                  
            for global_player in player_list:              
                if not global_player in tourament_list:
                    c.print("[bold yellow] Liste des joueurs disponibles:\n[bold yellow]")
                    value.append(f"{global_player.last_name}  {global_player.first_name}  classement = {global_player.rank}")
                     
                    for _ in range(len(value)):
                        counter += 1
                        key.append(counter)
                
                    players_availables = dict(zip(key,value))
                    
                    for k,v in players_availables.items():
                        c.print(f"[bold blue]- {k}: {v}[bold blue]\n")            
                
                    return players_availables
                
                else:
                    c.print("[bold red]Pas de joueurs disponibles dans la liste, pour ce tournois...[bold red]")
        else:
            c.print("[bold red]Aucun joueurs n'a été créé...[bold red]")
            
            
  