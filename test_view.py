from rich.console import Console


from test_controller import (TOUNAMENT_LIST,PLAYERS_LIST,
                             exit_main_menu, creat_tournament,
                             add_players)


c = Console()

starting_menu = True


def display_menu():
    choice = c.input("[bold yellow]Veuillez faire un choix:[bold yellow]\n\n"
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
        
    exit_main_menu(menu_choice)
    creat_tournament(menu_choice)
    add_players(menu_choice)
        
        

if __name__ == "__main__":
    while starting_menu:  
        display_the_menu = display_menu()
        choice_creat_tournament(display_the_menu)
        """
        print(TOUNAMENT_LIST)
        print(PLAYERS_LIST)
        """


    
    


























    
    
    
    
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