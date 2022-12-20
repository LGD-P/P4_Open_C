import sys
from rich.console import Console
from datetime import datetime

from dataclasses import dataclass

from MODEL import *


c = Console()
TOURNAMENT_LIST = [
    Tournament("Chess-Event","Paris",datetime.now().strftime("%d-%m-%Y"),
               [],[Players("DENIS", "Laurent", "11-12-2000","h",321,0)],
               "Blitz","Description",4)] 

@dataclass
class MenuController:
    choice_from_menu : str
    starting_menu : bool = True
    
    def quit_menu(self):
        c.print("[bold red]Merci à bientôt[bold red]")
        sys.exit()
        
        
    def creat_tournament(self):            
            nom = c.input("[bold green3]Entrez le nom du Tournois : [bold green3] ")
            date = datetime.now().strftime("%d-%m-%Y")
            place = c.input("[bold green3]Entrez le lieu du Tournois [bold green3] ")
            tours = []
            players= []
            time_control_dict = {1:"Bullet",2:"Blitz",3:"Coup rapide"}

            time_control= c.input("[bold green3]Choisissez le mode de contrôme "\
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
            c.print(TOURNAMENT_LIST)
    
    
    
    def add_player(self):
        last_name= c.input("[bold green3]Entrez le nom du Joueur: [bold green3] ")
        while last_name.isdigit():
            c.print("[bold red]\nInvalide, le nom ne peut pas contenir "\
                    "de numéro\n ")
            last_name= c.input("[bold green3]Entrez le nom du Joueur:"\
                "[bold green3] ")
                    
            
        first_name= c.input("[bold green3]Entrez le prénom du Joueur: "\
            "[bold green3] ")
        while first_name.isdigit():
            c.print("[bold red]\nInvalide, le prénom ne peut pas contenir "\
                    "de numéro\n ")
            first_name = c.input("[bold green3]Entrez le prénom du Joueur:"\
                "[bold green3] ")
    
    
        c.print("[bold green3]Entrez la date de naissance du joueur :")
        
        
        day = c.input("Jour: ")
        while not day.isdigit() or int(day) not in range(1,32):
            c.print("[bold red]\nInvalide: entrez un jour entre 1 et 31")
            day = c.input("Jour: ")
        
        month = c.input("Mois: ")
        while not month.isdigit() or int(month) not in range(1,13):
            c.print("[bold red]\nInvalide: entrez un jour entre 1 et 12")
            month = c.input("Mois: ")
    
                
        while int(month) == 2 and int(day) in range(29,32):
            c.print("[bold red] Le mois de février ne compte pas de 29 30 "\
            "ou 31[bold red]")
            
            day = c.input("Jour: ")
            while not day.isdigit() or int(day) not in range(1,32):
                c.print("[bold red]\nInvalide: entrez un jour entre 1 et 31")
                day = c.input("Jour: ")
                
            month = c.input("Mois: ")
            while not month.isdigit() or int(month) not in range(1,13):
                c.print("[bold red]\nInvalide: entrez un jour entre 1 et 12")
                month = c.input("Mois: ")
                    
        year = c.input("Année: ")
        while not year.isdigit() or not int(year) in range(
            (int(datetime.now().strftime("%Y"))-118),
            (int(datetime.now().strftime("%Y"))-10)) :
                c.print("[bold red]\nInvalide: Le joueur doit avoir "\
                    "au moins 10 ans, au plus 118 ans")
                year = c.input("Année: ")
        
        birth= (f'{day}-{month}-{year}')

        sex_list = ["h","f"]
        sex= c.input("[bold green3]Entrez le sexe: H - F[bold green3] ")
        while not sex.lower() in sex_list or sex.isdigit():
            c.print("[bold red]\nInvalide ")
            sex = c.input("[bold green3]Entrez le sexe du joueur: H / F "\
                "[bold green3]")
            
        rank= c.input("[bold green3]Entrez le classement du joueur:" \
            "[bold green3]")
                
        added_player = Players(last_name,first_name,str(birth),sex,int(rank),0)
        
        TOURNAMENT_LIST[0].players.append(added_player)
    
        print(TOURNAMENT_LIST[0].players)
    
action_after_choice = MenuController("")

        
        
