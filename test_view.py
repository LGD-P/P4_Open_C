from rich.console import Console


from test_controller import (exit_main_menu, creat_tournament,
                             add_players, Players,PLAYERS_LIST, TOURNAMENT_LIST)

from test_model import Tournament,Players


c = Console()

starting_menu = True


def display_menu():
    choice = c.input("\n[bold yellow]Veuillez faire un choix:[bold yellow]\n\n"
                    "[bold blue]- 1. Créer un tournois\n"
                    "- 2. Ajouter des joueurs\n"
                    "- 3. Lancer un tournois\n"
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
        
    
        
        

if __name__ == "__main__":
    while starting_menu:  
        display_the_menu = display_menu()
        choice_creat_tournament(display_the_menu)
        exit_main_menu(display_the_menu)
        creat_tournament(display_the_menu)
        add_players(display_the_menu)
    


###     FAITS:        ###
# Création d'un tournois ok
# Création de huit joueurs ok 
# Quitter le menu ok


###    A FAIRE:       ###
# Générer des paires 
# Entrer les résultats
# Gérer la base de données


