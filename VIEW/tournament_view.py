from rich.console import Console
from datetime import datetime

from MODEL.tournament_model import Tournament
from VIEW.player_view import PlayerView

c = Console()


class TournamentView:

    def display_add_tournament_form(self):
        nom = c.input(
            "[bold green3]Entrez le nom du Tournois : [bold green3] ")
        date = datetime.now().strftime("%d-%m-%Y")
        place = c.input(
            "[bold green3]Entrez le lieu du Tournois [bold green3] ")
        tours = []
        players = []
        time_control_dict = {1: "Bullet", 2: "Blitz", 3: "Coup rapide"}

        time_control = c.input("[bold green3]Choisissez le mode de contrôle "
                               "du temps\n[bold green3]"
                               "[bold green]- 1. Bullet\n"
                               "- 2. Blitz\n"
                               "- 3. Coup rapide\n[bold green]")

        while not time_control.isdigit() or int(time_control) <= 0 \
                or int(time_control) > 3:
            c.print("[bold red]\nInvalide, possiblités ==> 1. 2. 3. [bold red]\n")
            time_control = input(
                "- 1. Bullet\n"
                "- 2. Blitz\n"
                "- 3. Coup rapide\n"
            )

        time_control = time_control_dict[int(time_control)]

        description = c.input("[bold green3]Indiquez la description du tournois "
                              "[bold green3]")

        created_tournament = Tournament(nom, date, place, tours,
                                        players, time_control,
                                        description)

        return created_tournament

    def display_tournament_to_fill(self, tournament_list):
        if tournament_list:
            counter = -1
            for tournament in tournament_list:
                counter += 1
                c.print(f"- {counter}[bold green] {tournament.name}, "
                        f"{tournament.place}[bold green]\n")

            tournament_choice = c.input(
                "[bold blue]Faites votre choix :  [bold blue]"
            )

            while not tournament_choice.isdigit():
                tournament_choice = c.input(
                    "[bold red]Veillez faire un choix dans la liste[bold red]"
                )

            return tournament_choice

    """
    counter = -1
    value = []
    key = []
    if tournament_list:
    c.print("[bold yellow] Tournois disponibles : \n[bold yellow]")
    for tournament in tournament_list:
        value.append(f"{tournament.name},{tournament.place}")
    for _ in range(len(value)):
        counter += 1
        key.append(counter)

    tournaments_availables = dict(zip(key, value))

    for k, v in tournaments_availables.items():
        c.print(f"[bold bleu]- {k} : {v}[bold bleu]")

    return tournaments_availables
    """

    def display_add_player_in_tournament_form(self, tournament_list, player_list):
        self.tournament_view = TournamentView()
        self.player_view = PlayerView()

        if not tournament_list:

            c.print("[bold red]Veuillez créer un tournois pour "
                    "pouvoir l'alimenter en joueurs..\n [bold red]")

        elif not player_list:
            c.print("[bold red]Veuillez créer des joueurs pour "
                    "pouvoir les ajouter à des tournois")

        else:

            c.print("[bold blue]Choisissez un tournois dans lequel"
                    " ajouter un joueur: [bold blue]\n"
                    )

            tournament_choice = self.tournament_view.display_tournament_to_fill(
                tournament_list)

            print(type(tournament_choice))
            print(tournament_list[int(tournament_choice)])

            try:
                tournament_list[int(tournament_choice)]

            except IndexError:
                c.print(
                    "[bold red]Choisissez un tournois dans la liste: \n[bold red]")
                tournament_choice = self.tournament_view.display_tournament_to_fill(
                    tournament_list)

            tournament_choice = tournament_list[int(tournament_choice)]

            propose_players = self.player_view.display_players_to_choose(
                player_list, tournament_choice.players)
            # afficher seulement les joueurs qui ne sont pas dans le tournois 


"""
            if type(propose_players) == dict:
                player_choice = c.input(
                    "[bold yellow]Entrez le N° correspondant à votre choix [blod yellow]"
                )

                while not player_choice.isdigit() or not int(player_choice) in \
                        propose_players:
                    c.print("[bold red] Faites un choix dans la liste[bold red]")
                    player_choice = c.input(
                        "[bold red]==> [blod red]"
                    )

                player_choice = player_list[int(player_choice)]
                # n'afficher que les players qui ne sont pas déjà dans les tournois.
                while player_choice in tournament_choice.players:
                    c.print(
                        "[bold red] Ce joueur est déjà dans le tournois merci d'en"
                        "choisir un autre[bold red]")
                    player_choice = c.input(
                        "[bold red]==> [blod red]"
                    )

            tournament_choice.players.append(player_choice)

            print("****"*10)
            print("Affichage du tournois après alimentation: \n")
            print(tournament_choice)

            else:
                pass


# gérer les conditions d'affichage dans la view
"""
