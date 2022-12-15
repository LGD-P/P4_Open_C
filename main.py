import sys
from rich.console import Console

from classes_tournament_player import(Tournament, Player)



c = Console()

def display_menu():
    choice = c.input("[bold yellow]Veuillez faire un choix:[bold yellow]\n\n"
                    "[bold blue]- 1. Créer un tournois\n"
                    "- 2. Ajouter des joueurs\n"
                    "- 3. Lancer un tournoir\n"
                    "- 4. Ajouter des résultats\n"
                    "- 5. Montrer le rapport\n"
                    "- 6. Quitter\n\n[bold blue]"
                    )

    return choice



def choice_creat_tournament(menu_choice):
    
    while not menu_choice.isdigit() or int(menu_choice) <=0 or int(menu_choice) > 6:
        c.print("[bold red]\nInvalide, possiblités "
                "==> 1. 2. 3. 4. 5. 6. [bold red]\n ")
        
        menu_choice = display_menu()
        
    if int(menu_choice) == 6:
        sys.exit()
        
    if int(menu_choice) == 1:
        nom = input("Entrez le nom du Tournois : ")
        date = input("Entrez la date au format jj-mm-aaaa : ")
        place = input("Entrez le lieu du Tournois ")
        tours = []
        players= []
        time_control_dict = {1:"Bullet",2:"Blitz",3:"Coup rapide"}

        time_control= (input("Choisissez le mode de time-contrôle\n"                         
                            "- 1. Bullet\n"
                            "- 2. Blitz\n"
                            "- 3. Coup rapide\n"))



        while not time_control.isdigit() or int(time_control) <= 0 \
        or int(time_control) >3:
            c.print("[bold red]\nInvalide, possiblités ==> 1. 2. 3. [bold red]\n")
            time_control= input( 
            "- 1. Bullet\n"
            "- 2. Blitz\n"
            "- 3. Coup rapide\n"
            )

        time_control = time_control_dict[int(time_control)]
            
            
        description = input("Indiquez la description du tournois ")
        
        
        tournois = Tournament(nom,date,place,tours,
                            players,time_control,
                            description,
                            Tournament.number_of_rounds)
        
        return c.print(tournois)






if __name__ == "__main__":

    menu_choice = display_menu()
    choice_creat_tournament(menu_choice)
    


























    
    
    
    
'''  
    premier_tournois = Tournament("Paris_Game_Show",
                              "12-12-2022",
                              "Paris",
                              [],
                              [],
                              "Bullet",
                              "C'est LE tournois"
                              )

    player_1 = Player("Martin",
                    "Philippe",
                    "12-10-1980",
                    "M",
                    113)

    player_2 = Player("Durand",
                    "Denise",
                    "12-12-1985",
                    "M",
                    120)
    
    print(premier_tournois.display_tournament)
    NB_PLAYER = f"Le nom de joueur créé est {Player.counter}"
    print(NB_PLAYER)
'''