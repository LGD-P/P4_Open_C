from rich.console import Console

 
c = Console()


class TournamentView:
   
    def display_tournament(self, tournament_list):
        
        counter = -1
        value = []
        key = [] 
        if tournament_list:
            c.print("[bold yellow] Tournois disponibles : \n[bold yellow]")
            for tournament in tournament_list:
                value.append(f"{tournament.name},{tournament.place}")
            for _ in range(len(value)):
                counter +=1
                key.append(counter)
                
            tournaments_availables = dict(zip(key,value))
            
            for k,v in tournaments_availables.items():
                c.print(f"[bold bleu]- {k} : {v}[bold bleu]")
                
            return tournaments_availables
    
# gérer les conditions d'affichage dans la view 
