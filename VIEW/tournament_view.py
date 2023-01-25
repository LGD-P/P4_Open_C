from rich.console import Console
from datetime import datetime


from VIEW.player_view import PlayerView

c = Console()


class TournamentView:

    def display_add_tournament_form(self):
        name = c.input(
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

        return {
            "name": name,
            "date": date,
            "place": place,
            "tours": tours,
            "players": players,
            "time_control": time_control,
            "description": description
        }

    def display_tournament_to_fill(self, tournament_list):
        if tournament_list:
            for tournament in tournament_list:
                if not len(tournament.players) % 2:
                    c.print(f"{tournament_list.index(tournament)} [bold green]"
                            f"{tournament.name}, {tournament.place}[bold green]\n")
                    tournament_choice = c.input(
                        "[bold blue]Faites votre choix :  [bold blue]"
                    )

            while not tournament_choice.isdigit():
                tournament_choice = c.input(
                    "[bold red]Veillez faire un choix dans la liste[bold red]"
                )
            # retourner directement l'instance du tournois
            return tournament_choice

    def display_add_player_in_tournament_form(self, tournament_list, player_list):
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

            tournament_choice = self.display_tournament_to_fill(
                tournament_list)

            try:
                tournament_list[int(tournament_choice)]

            except IndexError:
                c.print(
                    "[bold red]Choisissez un tournois dans la liste: \n[bold red]")
                tournament_choice = self.tournament_view.display_tournament_to_fill(
                    tournament_list)

            tournament_choice = tournament_list[int(tournament_choice)]

            self.player_view.display_players_to_choose(
                player_list, tournament_choice.players)

            if tournament_choice.players == player_list:
                c.print(
                    "[bold red]Il n'y a pas de joueur dispinible pour "
                    "ce tournois.\n[bold red]")
            else:

                player_choice = c.input("[bold yellow]Choisissez votre joueur\n "
                                        " ==> [bold yellow]")

                while not player_choice.isdigit():
                    c.print(
                        "[bold red]Faites un choix parmis ceux disponibles[bold red]")
                    player_choice = c.input("[bold yellow]==> [bold yellow]")

                try:
                    player_list[int(player_choice)]
                except IndexError:
                    c.print(
                        "[bold red]Faites un choix parmis ceux disponibles[bold red]")
                    player_choice = c.input("[bold yellow]==> [bold yellow]")

                while player_list[int(player_choice)] in tournament_choice.players:
                    c.print(
                        "[bold red]Ce joueur est déjà dans la liste [bold red]")
                    player_choice = c.input("[bold yellow]==> [bold yellow]")

                """tournament_choice.players.append(
                    player_list[int(player_choice)])"""

                return {
                    "chosen_tournament": tournament_choice,
                    "chosen_player": player_list[int(player_choice)]
                }

    def display_choose_tournament_to_launch(self, tournament_list):
        if tournament_list:
            tournament_available = []

            for tournament in tournament_list:
                if not tournament.players:
                    c.print(
                        "[bold red]Vous devez ajouter des joueurs d'abord...\n[bold red]")
                else:

                    if len(tournament.players) != 0 and not len(tournament.players) % 2:
                        tournament_available.append(tournament)

                        c.print(f"{tournament_list.index(tournament)} [bold green]"
                                f"{tournament.name}, {tournament.place}[bold green]\n")
                        tournament_choice = c.input(
                            "[bold blue]Faites votre choix :  [bold blue]"
                        )

                        choice_list = []
                        index = -1
                        for element in tournament_available:
                            index += 1
                            choice_list.append(index)

                        while not tournament_choice.isdigit() or not \
                                int(tournament_choice) in choice_list:
                            c.print(
                                '[bold red] Merci de faire un choix dans la liste[bold red]')
                            tournament_choice = c.input("==> ")

                        tournament_to_launch = tournament_available[int(
                            tournament_choice)]

                        return tournament_to_launch

                    else:
                        c.print(f"{tournament_list.index(tournament)} "
                                f"[bold green] {tournament.name}, {tournament.place} "
                                "[bold green][bold red] Pas assez de joueurs dans le "
                                "tournois [bold red]\n")

        else:
            c.print("[bold red]Vous devez créer un tournois d'abord...\n[bold red]")
            pass
