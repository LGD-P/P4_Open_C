import sys
from rich.console import Console
from datetime import datetime

from dataclasses import dataclass

from MODEL import *


c = Console()

TOURNAMENT_LIST = [Tournament("Chess-Event","Paris",datetime.now().strftime("%d-%m-%Y"),
                              [],[
                                  Players("DENIS", "Laurent", "11-12-2000","h",321,0),
                                  Players("LAURENT", "Denis", "11-10-2005","h",123,0),
                                  Players("MOINE", "Alice", "10-10-1990","f",100,0),
                                  Players("VAULT", "Lise", "01-02-1980","f",10,0),
                                  Players("CREPIN", "Maurice", "12-07-1950","h",40,0),
                                  Players("TIAGO", "Daniela", "05-06-1977","f",35,0),
                                  Players("EDON", "Gabrielle", "09-03-1985","f",25,0)
                                  ],"Blitz","Description",4)] 

@dataclass
class MenuController:
    choice_from_menu : str    
    
    def quit_menu(self):
        c.print("[bold red]Merci à bientôt[bold red]")
        sys.exit()  
        
        
action_to_quit = MenuController("")
        
@dataclass
class TournamentController:
    choice_from_menu : str       
    
    # Si cette fonction est placé dans la classe 
    # TournamentView je ne peux pas l'appelle au moment d'instancier 
    # la classe TournamentVieu
    def display_tournament_list(self):
        counter = 0
        for tournois in TOURNAMENT_LIST:
            counter +=1
            c.print(f"\nTounois N°{counter} : {tournois.name}")
            
            
    def add_tournament(self):
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
            
            
            tournois = Tournament(nom,date,place,tours,
                                players,time_control,
                                description,
                                Tournament.number_of_rounds)
            
            TOURNAMENT_LIST.append(tournois)

            c.print(f"\nMerci, votre tournois est créé :\n "
                    f"[bold yellow]{tournois.display_tournament}[bold yellow]")
                

action_in_tournmanent_menu = TournamentController("")