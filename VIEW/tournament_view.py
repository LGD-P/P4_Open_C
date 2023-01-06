from rich.console import Console
from datetime import datetime

from MODEL.tournament_model import Tournament
 
c = Console()


class TournamentView:
    
    def display_tournament_form(self):
        nom = c.input("[bold green3]Entrez le nom du Tournois : [bold green3] ")
        date = datetime.now().strftime("%d-%m-%Y")
        place = c.input("[bold green3]Entrez le lieu du Tournois [bold green3] ")
        tours = []
        players= []
        time_control_dict = {1:"Bullet",2:"Blitz",3:"Coup rapide"}

        time_control= c.input("[bold green3]Choisissez le mode de contrôle "\
            "du temps\n[bold green3]"\
                "[bold green]- 1. Bullet\n"
                "- 2. Blitz\n"
                "- 3. Coup rapide\n[bold green]")

        while not time_control.isdigit() or int(time_control) <= 0 \
        or int(time_control) >3:
            c.print("[bold red]\nInvalide, possiblités ==> 1. 2. 3. [bold red]\n")
            time_control= input( 
            "- 1. Bullet\n"
            "- 2. Blitz\n"
            "- 3. Coup rapide\n"
            )

        time_control = time_control_dict[int(time_control)]
            
            
        description = c.input("[bold green3]Indiquez la description du tournois "\
            "[bold green3]")
        
        
        created_tournament = Tournament(nom,date,place,tours,
                                        players,time_control,
                                        description)
        
        return created_tournament

   
   
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




