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
                                  Players("EDON", "Gabrielle", "09-03-1985","f",25,0),
                                  Players("PATTON", "Gabriel", "09-03-1970","h",20,0)
                                  ],"Blitz","Description",4), 
                   Tournament("Chess-Show","Moscow",datetime.now().strftime("%d-%m-%Y"),
                              [],[],"Blitz","Description",4)
                   ]] 

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
    
    def display_tournament_list(self):
        counter = 0
        for tournois in TOURNAMENT_LIST:
            counter +=1
            c.print(f"\nTounois N°{counter} : {tournois.name}\n"
                    f"\n Joueur : {tournois.players} ")
            
            
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
                

TOURNAMENT_CONTROLLER = TournamentController("")



@dataclass
class PlayerController:
    choice_from_menu : str 
    
    
    def add_player(self):
        if not TOURNAMENT_LIST:
            c.print("[bold red] Il vous faut d'abord créer un tournois "\
                "pour pouvoir y ajouter des joueurs.[bold red]")
            
            
        else:             
            c.print(f"\n[bold yellow]Liste des tournois disponible :\n\n[bold yellow]")
            tournament_list_choice = []
            for tournois in TOURNAMENT_LIST:
                if not len(tournois.players) == 8:
                    tournament_list_choice.append(TOURNAMENT_LIST.index(tournois) + 1)
                    c.print(f"[bold blue]- N°{TOURNAMENT_LIST.index(tournois) + 1} :"
                            f" {tournois.name}\n[bold blue]")
                
            tournament_choice = c.input("[bold yellow]Entrez le N° du tournois"\
            " dans lequel vous souhaitez ajouter des joueurs. \n[bold yellow]")
            

            while not int(tournament_choice) in tournament_list_choice:
                tournament_choice = c.input("[bold red]Entrez le N° d'un"\
            " tournois proposé dans la liste. \n[bold red]")
            
            """
            try:
                TOURNAMENT_LIST[int(tournament_choice)]
            except IndexError:
                tournament_choice = c.input("[bold red]Entrez le N° d'un"\
                " tournois existant. \n[bold red]")
            """
                    
            result = TOURNAMENT_LIST[int(tournament_choice) - 1]
            
          
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
            
            result.players.append(added_player)


    def display_player_listing(self):
        for element in TOURNAMENT_LIST:
            c.print(element.players)
        
        
"""        
      
    def select_tournament_for_player(self):
        counter = 0
        c.print(f"\n[bold yellow]Tournois disponible(s):\n\n[bold yellow]")
        for tournois in TOURNAMENT_LIST:
            if len(tournois.players) < 8:
            counter += 1
            c.print(f"[bold blue]- {counter} : {tournois.name}\n[bold blue]")
            
        tournament_choice = c.input("[bold yellow]Entrez le N° du tournois"\
            " dans lequel vous souhaitez ajouter des joueurs. \n[bold yellow]")
            
        try:
            TOURNAMENT_LIST[int(tournament_choice)]
        except IndexError:
            tournament_choice = c.input("[bold red]Entrez le N° d'un"\
            " tournois existant. \n[bold red]")
                
        result = TOURNAMENT_LIST[int(tournament_choice) - 1]
        return result
            
"""           
            
        
        
PLAYER_CONTROLLER = PlayerController("")