from rich.console import Console
from datetime import datetime


c = Console()


class TournamentView:

    def display_add_tournament_form(self):
        """
        This function take user input to fill player settings

        Returns:
            dict : {'player attributes' : user input}
        """
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
            c.print("[bold red]\nInvalide, possiblités ==> 1. 2. 3. "
                    "[bold red]\n")
            time_control = input(
                "- 1. Bullet\n"
                "- 2. Blitz\n"
                "- 3. Coup rapide\n"
            )

        time_control = time_control_dict[int(time_control)]

        description = c.input("[bold green3]Indiquez la description du "
                              "tournois [bold green3]")

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
        """
        This function display tournament available
        User choose one and can fill it with players

        Args:
            tournament_list (list): list of each tournament instance created

        Returns:
            instance: tournament
        """

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

            while not tournament_choice.isdigit() \
                    or not int(tournament_choice) \
                    in choice_tournament_available:
                tournament_choice = c.input(
                    "[bold red]Veillez faire un choix dans la liste[bold red]"
                )

            # retourner directement l'instance du tournois
            return tournament_list[int(tournament_choice)]

    def display_add_player_in_tournament_form(self, tournament_list,
                                              player_list, player_view):
        """
        This function display only players available to fill tournament with
        returning a dict with tournament and player choosen

        Args:
            tournament_list (list): list of each tournament instance created
            player_view (instance): view instance to use player_view method
            and display player tournament_list (list): list of each player
            instance created

        Returns:
            dict: {
                    "chosen_tournament": tournament instance ,
                    "chosen_player": player instance
                }
        """
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
                    "[bold red] Il n'y a pas de joueur disponible pour "
                    "ce tournois.\n[bold red]")
                return None

            else:

                player_view.display_players_to_choose(
                    player_list, tournament_list)

                player_choice = c.input("[bold yellow]Choisissez votre "
                                        "joueur\n ==> [bold yellow]")
                choice_list = []
                for player in player_list:
                    choice_list.append(player_list.index(player))

                while not player_choice.isdigit() \
                        or int(player_choice) not in choice_list:
                    c.print(
                        "[bold red]Faites un choix parmis ceux "
                        "disponibles[bold red]")
                    player_choice = c.input("[bold yellow]==> [bold yellow]")

                while player_list[int(player_choice)] in tournament.players:
                    c.print(
                        "[bold red]Ce joueur est déjà dans la liste "
                        "[bold red]")
                    player_choice = c.input("[bold yellow]==> [bold yellow]")

                # tournament_choice.players.append(
                    # player_list[int(player_choice)])

                # c.print(player_list[int(player_choice)])

                return {
                    "chosen_tournament": tournament,
                    "chosen_player": player_list[int(player_choice)]
                }

    def display_choose_a_tournament_to_launch(self, tournament_list):
        """
        This function check the tournament list and propose user to launch one

        Args:
            tournament_list (list): list of each tournament instance created

        Returns:
            instance: tournament instance
        """
        if tournament_list:
            tournament_available = []

            for tournament in tournament_list:
                if not tournament.players:
                    c.print(
                        "[bold red]Vous devez ajouter des joueurs d'abord..."
                        "\n[bold red]")

                else:

                    if len(tournament.players) != 0 \
                            and not len(tournament.players) % 2:
                        tournament_available.append(tournament)

                        c.print(
                            f"{tournament_list.index(tournament)} [bold green]"
                            f"{tournament.name}, {tournament.place}"
                            "[bold green]\n")
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
                                "[bold red] Merci de faire un choix dans "
                                "la liste[bold red]")
                            tournament_choice = c.input("==> ")

                        tournament_to_launch = tournament_available[int(
                            tournament_choice)]

                        return tournament_to_launch

                    else:
                        c.print(f"{tournament_list.index(tournament)} "
                                f"[bold green] {tournament.name}, "
                                f"{tournament.place} "
                                "[bold green][bold red] Pas assez de joueurs"
                                "dans le tournois [bold red]\n")

        else:
            c.print("[bold red]Vous devez créer un tournois d'abord..."
                    "\n[bold red]")
            return None

    def report_display_players_in_tournament_by_alphabetical_order(
            self, tournament_list):
        """
        This function used in report return player list by alphabetical order
        using player list in tournament

        Args:
            tournament_list (list): list of each tournament instance created

        Returns:
            list: list of player in tournament sorted by alphabetical order
        """
        answer = []
        for tournament in tournament_list:
            answer.append(tournament_list.index(tournament))
            question = c.input("[bold yellow]Choisissez le tournois dont vous"
                               " souhaitez afficher les joueurs par ordre "
                               "alphabétique\n[bold yellow]"
                               f"[bold blue] "
                               f"- {tournament_list.index(tournament)} : "
                               f"{tournament.name}\n[bold blue]")

            while not question.isdigit() or not int(question) in answer:
                question = c.input(
                    "[bold red]Faites un choix dans la liste :[bold red]\n\n"
                    f" - {tournament_list.index(tournament)} : {tournament}")

            tournament_choosen = tournament_list[int(question)]

            sorted_players = sorted(tournament_choosen.players,
                                    key=lambda player: player.last_name)

            return sorted_players

    def report_display_players_in_tournament_by_rank(self, tournament_list):
        """
        This function used in report return player list by rank, using player
        list in tournament

        Args:
            tournament_list (_type_): list of each tournament instance created

        Returns:
            list : list of player in tournament sorted by rank
        """
        answer = []
        for tournament in tournament_list:
            answer.append(tournament_list.index(tournament))
            question = c.input("[bold yellow]Choisissez le tournois dont "
                               "vous souhaitez afficher les joueurs par "
                               "rang\n[bold yellow] "
                               f"[bold blue]"
                               f" - {tournament_list.index(tournament)} : "
                               f"{tournament.name}\n[bold blue]")

            while not question.isdigit() or not int(question) in answer:
                question = c.input(
                    "[bold red]Faites un choix dans la liste :[bold red]\n\n"
                    f" - {tournament_list.index(tournament)} : {tournament}")

            tournament_choosen = tournament_list[int(question)]

            sorted_players = sorted(tournament_choosen.players,
                                    key=lambda player: player.rank)

            return sorted_players

    def report_display_tournament_list(self, tournament_list):
        """
        This function used in report return tournament list

        Args:
            tournament_list (_type_): list of each tournament instance created
        """
        c.print("[bold magenta]Voici la liste des tournois : \n"
                "[bold magenta]")
        index = 0
        for tournament in tournament_list:
            index += 1
            c.print(
                f"Tournois N°{index}: \n {tournament.__repr__()}")

    def report_display_tour_in_tournament(self, tournament_list, round_list):
        """
        This function used in report return each round in and tournament
        selected

        Args:
            tournament_list (list): list of each tournament instance created
            round_list (list): list of each round instance created in
            tournament

        Returns:
            list: list of each round instance created in tournament
        """

        answer = []
        for tournament in tournament_list:
            answer.append(tournament_list.index(tournament))
            question = c.input("[bold yellow]Choisissez le tournois dont "
                               "vous souhaitez afficher la liste des tours "
                               "alphabétique\n[bold yellow]"
                               "[bold blue] "
                               f"- {tournament_list.index(tournament)} : "
                               f"{tournament.name}\n[bold blue]")

            while not question.isdigit() or not int(question) in answer:
                question = c.input(
                    "[bold red]Faites un choix dans la liste :[bold red]\n\n"
                    f" - {tournament_list.index(tournament)} : {tournament}")

            tournament_choosen = tournament_list[int(question)]

            round_list_to_display = []
            for round in round_list:

                if tournament_choosen.name in round.tournament_name:

                    round_list_to_display.append(round)

            return round_list_to_display

    def report_display_match_in_tournament(self, tournament_list):
        """
        This function used in report return each matchs played between each
        players in tournament

        Args:
            tournament_list (list): list of each tournament instance created

        Returns:
            list: attribute of tournament selected as list of each match
            in tournament.
        """
        answer = []
        for tournament in tournament_list:
            answer.append(tournament_list.index(tournament))
            question = c.input("[bold yellow]Choisissez le tournois dont "
                               "vous souhaitez afficher la liste des matchs"
                               "\n[bold yellow]"
                               "[bold blue]"
                               f"- {tournament_list.index(tournament)} : "
                               f"{tournament.name}\n[bold blue]")

            while not question.isdigit() or not int(question) in answer:
                question = c.input(
                    "[bold red]Faites un choix dans la liste :[bold red]\n\n"
                    f" - {tournament_list.index(tournament)} : {tournament}")

            tournament_choosen = tournament_list[int(question)]

            return tournament_choosen.tours

    def display_report(self, tournament_list, round_list):
        """
        This report function user all precedents functions and displayer user
        choice
        Args:
            tournament_list (list): list of each tournament instance created
            round_list (list): list of each round instance created in
            tournament
        """
        question = c.input("[bold yellow]  Que souhaitez-vous consulter ?"
                           "[bold yellow]\n\n "
                           "[bold blue]- 01. Liste de tous les joueurs d'un "
                           "tournoi par ordre alphabétique\n "
                           "- 02. Liste de tous les joueurs d'un tournoi par "
                           "classement\n "
                           "- 03. Liste de tous les tournois.\n "
                           "- 04. Liste de tous les tours d'un tournoi.\n "
                           "- 05. Liste de tous les matchs d'un tournoi.\n"
                           "[bold blue]")

        answer = [1, 2, 3, 4, 5]

        while not question.isdigit() or not int(question) in answer:
            question = c.input("[bold red]Faites un choix dans la liste...\n"
                               "\n [bold red]"
                               "[bold yellow]  Que souhaitez-vous consulter ?"
                               "[bold yellow]\n\n "
                               "[bold blue]- 01. Liste de tous les joueurs "
                               "d'un tournoi par ordre alphabétique\n "
                               "- 02. Liste de tous les joueurs d'un tournoi "
                               "par classement\n "
                               "- 03. Liste de tous les tournois.\n "
                               "- 04. Liste de tous les tours d'un tournoi.\n "
                               "- 05. Liste de tous les matchs d'un tournoi."
                               "\n[bold blue]")

        if int(question) == 1:
            players_list = self \
                .report_display_players_in_tournament_by_alphabetical_order(
                    tournament_list)
            c.print("[green3]Voici les joueurs :\n[green3]")

            for players in players_list:
                c.print(players)

        elif int(question) == 2:
            players_list = self.report_display_players_in_tournament_by_rank(
                tournament_list)
            c.print("[green3]Voici les joueurs :\n[green3]")

            for players in players_list:
                c.print(players)

        elif int(question) == 3:
            self.report_display_tournament_list(tournament_list)

        elif int(question) == 4:
            list_of_tours = self.report_display_tour_in_tournament(
                tournament_list, round_list)

            c.print("[green3]Voici les rounds du tournois : [green3]\n")
            for round in list_of_tours:
                c.print(str(round))

        elif int(question) == 5:
            list_of_tours = self.report_display_match_in_tournament(
                tournament_list)
            index = 0
            for tour in list_of_tours:
                index += 1
                c.print(f"[green3] Dans le tour N°{index}\n[green3]\n")
                for match in tour:
                    c.print(
                        f"{match[0].last_name} {match[0].first_name} "
                        "a affronté ==>"
                        f" {match[1].last_name} {match[1].first_name} \n")
