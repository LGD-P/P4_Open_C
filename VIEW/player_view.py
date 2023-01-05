from rich.console import Console

 
c = Console()


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