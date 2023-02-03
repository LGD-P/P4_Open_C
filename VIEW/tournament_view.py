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
            "description": description,
            "player_score": {}
        }

    def display_tournament_to_fill(self, tournament_list):
        if tournament_list:
            index = -1
            for tournament in tournament_list:
                choice_tournament_available = []
                index += 1
                choice_tournament_available.append(index)
                # if not len(tournament.players) % 2:
                c.print(f"{tournament_list.index(tournament)} [bold green]"
                        f"{tournament.name}, {tournament.place}[bold green]\n")
                tournament_choice = c.input(
                    "[bold blue]Faites votre choix :  [bold blue]"
                )

            while not tournament_choice.isdigit() or not int(tournament_choice) in choice_tournament_available:
                tournament_choice = c.input(
                    "[bold red]Veillez faire un choix dans la liste[bold red]"
                )

            # retourner directement l'instance du tournois
            return tournament_list[int(tournament_choice)]

    def display_add_player_in_tournament_form(self, tournament_list, player_list):
        self.player_view = PlayerView()

        if not tournament_list:

            c.print("[bold red]Veuillez créer un tournois pour "
                    "pouvoir l'alimenter en joueurs..\n [bold red]")
            return None

        elif not player_list:
            c.print("[bold red]Veuillez créer des joueurs pour "
                    "pouvoir les ajouter à des tournois")
            return None

        else:

            c.print("[bold blue]Choisissez un tournois dans lequel"
                    " ajouter un joueur: [bold blue]\n"
                    )

            tournament = self.display_tournament_to_fill(
                tournament_list)

            if len(tournament.players) == len(player_list):
                c.print(
                    "[bold red]Il n'y a pas de joueur disponible pour "
                    "ce tournois.\n[bold red]")
                return None

            else:

                self.player_view.display_players_to_choose(
                    player_list, tournament_list)

                player_choice = c.input("[bold yellow]Choisissez votre joueur\n "
                                        " ==> [bold yellow]")
                choice_list = []
                for player in player_list:
                    choice_list.append(player_list.index(player))

                while not player_choice.isdigit() or int(player_choice) not in choice_list:
                    c.print(
                        "[bold red]Faites un choix parmis ceux disponibles[bold red]")
                    player_choice = c.input("[bold yellow]==> [bold yellow]")

                while player_list[int(player_choice)] in tournament.players:
                    c.print(
                        "[bold red]Ce joueur est déjà dans la liste [bold red]")
                    player_choice = c.input("[bold yellow]==> [bold yellow]")

                """tournament_choice.players.append(
                    player_list[int(player_choice)])"""

                return {
                    "chosen_tournament": tournament,
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

                        choice_player = []
                        index = -1
                        for _ in tournament_available:
                            index += 1
                            choice_player.append(index)

                        while not tournament_choice.isdigit() or not \
                                int(tournament_choice) in choice_player:
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
            return None

    def display_players_in_tounrnament_by_alphabetical_order(self, tournament_list):
        answer = []
        for tournament in tournament_list:
            answer.append(tournament_list.index(tournament))
            question = c.input("[bold yellow]Choisissez le tournois dont vous "
                               "souhaitez afficher les joueurs par ordre "
                               "alphabétique\n[bold yellow]"
                               f"[bold blue] - {tournament_list.index(tournament)} : "
                               f"{tournament.name}\n[bold blue]")

            while not question.isdigit() or not int(question) in answer:
                question = c.input("[bold red]Faites un choix dans la liste :[bold red]\n\n"
                                   f" - {tournament_list.index(tournament)} : {tournament}")

            tournament_choosen = tournament_list[int(question)]

            sorted_players = sorted(tournament_choosen.players,
                                    key=lambda player: player.last_name)

            return sorted_players

    def display_players_in_tournament_by_rank(self, tournament_list):
        answer = []
        for tournament in tournament_list:
            answer.append(tournament_list.index(tournament))
            question = c.input("[bold yellow]Choisissez le tournois dont vous "
                               "souhaitez afficher les joueurs par rang\n[bold yellow]"
                               f"[bold blue] - {tournament_list.index(tournament)} : "
                               f"{tournament.name}\n[bold blue]")

            while not question.isdigit() or not int(question) in answer:
                question = c.input("[bold red]Faites un choix dans la liste :[bold red]\n\n"
                                   f" - {tournament_list.index(tournament)} : {tournament}")

            tournament_choosen = tournament_list[int(question)]

            sorted_players = sorted(tournament_choosen.players,
                                    key=lambda player: player.rank)

            return sorted_players

    def display_tournament_list(self):
        return None

    def display_tour_in_tournament(self):
        return None

    def display_match_in_tournament(self):
        return None

    def display_report(self, tournament_list):
        question = c.input("[bold yellow]  Que souhaitez-vous consulter ?[bold yellow]\n\n "
                           "[bold blue]- 01. Liste de tous les joueurs d'un tournoi par ordre alphabétique\n "
                           "- 02. Liste de tous les joueurs d'un tournoi par classement\n "
                           "- 03. Liste de tous les tournois.\n "
                           "- 04. Liste de tous les tours d'un tournoi.\n "
                           "- 05. Liste de tous les matchs d'un tournoi.\n[bold blue]")

        answer = [1, 2, 3, 4, 5]

        while not question.isdigit() or not int(question) in answer:
            question = c.input("[bold red]Faites un choix dans la liste...\n\n [bold red]"
                               "[bold yellow]  Que souhaitez-vous consulter ?[bold yellow]\n\n "
                               "[bold blue]- 01. Liste de tous les joueurs d'un tournoi par ordre alphabétique\n "
                               "- 02. Liste de tous les joueurs d'un tournoi par classement\n "
                               "- 03. Liste de tous les tournois.\n "
                               "- 04. Liste de tous les tours d'un tournoi.\n "
                               "- 05. Liste de tous les matchs d'un tournoi.\n[bold blue]")

        if int(question) == 1:
            players_list = self.display_players_in_tounrnament_by_alphabetical_order(
                tournament_list)
            c.print("[bold magenta]Voici les joueurs :\n[bold magenta]")

            for players in players_list:
                c.print(players)

        elif int(question) == 2:
            players_list = self.display_players_in_tournament_by_rank(
                tournament_list)
            c.print("[bold magenta]Voici les joueurs :\n[bold magenta]")

            for players in players_list:
                c.print(players)
