from rich.console import Console
from datetime import datetime
import sys

from MODEL_V3 import Tournament, Players

from VIEW_V3 import MenuView, PlayerView, TournamentView

c = Console()  


def quit_menu():
    c.print("[bold red]Merci à bientôt[bold red]")
    sys.exit() 
        
class MenuController:
    def __init__(self):
        self.menu_view_in_controller = MenuView({
    "1":{
        "label":"[bold blue]- 1. Créer des tournois :pencil: [bold blue]",
        "action":TournamentController().add_tournament,
            },
    "2":{
        "label":"[bold blue]- 2. Créer des joueurs :pencil: [bold blue]",
        "action":PlayersController().add_player,
            },
    "3":{
        "label":"[bold blue]- 4. Ajouter des joueurs à un tournois :pencil:[bold blue]",
            "action":PlayersController().add_player_in_tournament,
            },
    "4":{
        "label":"[bold blue]- 3. Lancer un tournois :watch:[bold blue]",
            "action":"",
            },
    "5":{
        "label":"[bold blue]- 5. Ajouter des résultats :trophy: [bold blue]",
        "action":"",
            },
    "6":{
        "label":"[bold blue]- 6. Montrer le rapport :bar_chart: [bold blue]",
        "action":"",
            },
    "7":{
        "label":"[bold blue]- 7. Quitter :raising_hand: \n [bold blue]",
        "action": quit_menu
            }
    })


    def run_program(self, running_program=True):
        while running_program:
            self.menu_view_in_controller.display_menu_and_get_choice()
     

      
class TournamentController:
    def __init__(self,) :
           self.tournament_list_controller = TournamentView([
            Tournament("Chess-Show","Moscow",datetime.now().strftime("%d-%m-%Y"),
                       [],[],"Blitz","Description",4
                       ),
            Tournament("Chess-Show N°2","Paris",datetime.now().strftime("%d-%m-%Y"),
            [],[],"Blitz","Description N°2",4)
            ])
           
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
                                description)
            
            self.tournament_list_controller.tournament_list_view.append(tournois)
            
            c.print(self.tournament_list_controller.tournament_list_view)
 
 
                    
   






class PlayersController:
    def __init__(self):
        self.players_list_controller = PlayerView([
            Players("DENIS", "Laurent", "11-12-2000","h",321,0),
            Players("LAURENT", "Denis", "11-10-2005","h",123,0),
            Players("MOINE", "Alice", "10-10-1990","f",100,0),
            Players("VAULT", "Lise", "01-02-1980","f",10,0),
            Players("CREPIN", "Maurice", "12-07-1950","h",40,0),
            Players("TIAGO", "Daniela", "05-06-1977","f",35,0),
            Players("EDON", "Gabrielle", "09-03-1985","f",25,0),
            Players("PATTON", "Gabriel", "09-03-1970","h",20,0),
            Players("LEROY", "Anatole","17/10/1975","h",2,0)
        ])

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
        
        self.players_list_controller.players_list_view.append(choice_2)
        
        print(self.players_list_controller.players_list_view)
        
        
    def add_player_in_tournament(self):
        self.players_list_controller.display_players_to_choose()
        choice = c.input(
            "[bold yellow]Entrez le N° correspondant à votre choix [blod yellow]"
            )

