from rich.console import Console
from datetime import datetime
import sys

from MODEL_V3 import Tournament, Players

from VIEW_V3 import MenuView

c = Console()  


def quit_menu():
    c.print("[bold red]Merci à bientôt[bold red]")
    sys.exit() 
        
class MenuController:
    def __init__(self):
        self.menu_view_in_controller = MenuView({
    "1":{
        "label":"[bold blue]- 1. Gérer des tournois :pencil: [bold blue]",
        "action":"",
            },
    "2":{
        "label":"[bold blue]- 2. Ajouter des joueurs :pencil: [bold blue]",
        "action":PlayersController().add_player,
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
        "action": quit_menu
            }
    })



        
    def run_program(self, running_program=True):
        while running_program:
            self.menu_view_in_controller.display_menu_and_get_choice()

        

class PlayersController:
    def __init__(self,players_list = []):
        self.players_list = players_list
        
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
                
        choice_2 = Players(last_name,first_name,str(birth),sex,int(rank),0)
        
        self.players_list.append(choice_2)
        
        print(self.players_list)