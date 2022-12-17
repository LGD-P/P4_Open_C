import sys
from datetime import datetime
from rich.console import Console

from test_model import Players, Tournament

TOUNAMENT_LIST = []
PLAYERS_LIST = [1,2,3,4,5,6,7,8]

c = Console()


        

def creat_tournament(menu_choice):
    if int(menu_choice) == 1:
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
                                Tournament.nu)

        
            TOUNAMENT_LIST.append(tournois)
            
            c.print(f"\nMerci, votre tournois est créer :\n "
                    f"[bold yellow]{tournois.display_tournament}[bold yellow]")
            
            
def add_players(menu_choice):
    if len(PLAYERS_LIST) == 8:
        c.print("[bold red]Vous avez déjà huit joueurs\n"
                "le tournois est plein[bold red]")
        pass
    
    elif int(menu_choice) == 2:
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
        
            birth= c.input("[bold green3]Entrez l'age du joueur:"\
                "jj-mm-aaaa[bold green3]")
    
            sex_list = ["h","f"]
            sex= c.input("[bold green3]Entrez le sexe: H - F[bold green3] ")
            while not sex.lower() in sex_list or sex.isdigit():
                c.print("[bold red]\nInvalide ")
                sex = c.input("[bold green3]Entrez le sexe du joueur: H / F "\
                    "[bold green3]")
                
            rank= c.input("[bold green3]Entrez le classement du joueur: [bold green3]")
            
            player =  Players(last_name,first_name,birth,sex,rank)
            
            PLAYERS_LIST.append(player)
            
            c.print(player.number_of_player_created)
            
            
def exit_main_menu(menu_choice):
    if int(menu_choice) == 6:
        sys.exit()  
                