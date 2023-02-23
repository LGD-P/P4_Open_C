from rich.console import Console


from VIEW.match_view import MatchView
from VIEW.round_view import RoundView


c = Console()


class Report_View:

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
        answer = [tournament_list.index(
            tournament) for tournament in tournament_list if tournament.players]

        tournament_available = [
            tournament for tournament in tournament_list if tournament.players]

        if not tournament_available:
            c.print(
                "[bold red]Il faut ajouter des joueurs aux tournois [bold red]")
            return None

        for tournament in tournament_available:
            if tournament in tournament_list:
                c.print(f"[bold blue]"
                        f" - {tournament_list.index(tournament)} : "
                        f"{tournament.name}\n[bold blue]")

        question = c.input("[bold yellow]Choisissez le N° du tournois dont "
                           "vous souhaitez afficher les joueurs par "
                           "rang\n[bold yellow] "
                           )

        while not question.isdigit() or not int(question) in answer:
            question = c.input(
                "[bold red]Faites un choix dans la liste :[bold red]\n\n"
                f" - {tournament_list.index(tournament)} : {tournament}")

        tournament_choosen = tournament_list[int(question)]

        sorted_players = sorted(tournament_choosen.players,
                                key=lambda player: player.last_name)

        c.print("[bold magenta]Voici la liste des joueurs par ordre "
                "alphabétique:\n[bold magenta]")
        for player in sorted_players:
            c.print(player)

    def report_display_players_in_tournament_by_rank(self, tournament_list):
        """
        This function used in report return player list by rank, using player
        list in tournament

        Args:
            tournament_list (_type_): list of each tournament instance created

        Returns:
            list : list of player in tournament sorted by rank
        """
        answer = [tournament_list.index(
            tournament) for tournament in tournament_list if tournament.players]
        tournament_available = [
            tournament for tournament in tournament_list if tournament.players]

        if not tournament_available:
            c.print(
                "[bold red]Il faut ajouter des joueurs aux tournois [bold red]")
            return None

        for tournament in tournament_available:
            if tournament in tournament_list:
                c.print(f"[bold blue]"
                        f" - {tournament_list.index(tournament)} : "
                        f"{tournament.name}\n[bold blue]")

        question = c.input("[bold yellow]Choisissez le N° du tournois dont "
                           "vous souhaitez afficher les joueurs par "
                           "rang\n[bold yellow] "
                           )

        while not question.isdigit() or not int(question) in answer:
            question = c.input(
                "[bold red]Faites un choix dans la liste :[bold red]\n\n")

        tournament_choosen = tournament_list[int(question)]

        sorted_players = sorted(tournament_choosen.players,
                                key=lambda player: player.rank)

        c.print("[bold magenta]Voici la liste des joueurs par rang:"
                "\n[bold magenta]")

        for player in sorted_players:

            c.print(
                f"[white]- {player.last_name} {player.first_name}[white] "
                "[bold yellow] Classement :[bold yellow] "
                f"[white]{player.rank}[white]")

    def display_player_in_row(self, tournament_list):
        """Display players from tournament list

        Args:
            tournament_list (list):  tournament list 
        """
        for tournament in tournament_list:
            for player in tournament.players:
                c.print(player)

    def display_player_score(self, tournament):
        """Displayer player score from tournament

        Args:
            tournament (instance): from loop on tournament_list
        """

        for player_score in tournament.player_score:
            c.print(
                f"[bold cyan]{player_score.last_name} "
                f"{player_score.first_name}[bold cyan][bold yellow], "
                "SCORE ==>  [bold yellow]"
                f"[bold cyan]{tournament.player_score[player_score]}"
                "[bold cyan]")

    def display_tournament(self, tournament_list):
        """Pretty display of each tournament

        Args:
            tournament_list (list): tournament_list from 
        """

        for tournament in tournament_list:
            c.print("[bold red]         ---TOUNOIS N°"
                    f"{int(tournament_list.index(tournament)+1)}---\n[bold red]")

            c.print("[bold green3]Nom du tournois : [bold green3]"
                    f"[bold yellow]{tournament.name}[bold yellow]")

            c.print("[bold green3]Lieu du tournois :[bold green3]"
                    f"[bold yellow]{tournament.place}[bold yellow]")

            c.print("[bold green3]Date du tournois : [bold green3]"
                    f"[bold yellow]{tournament.date}[bold yellow]0")

            c.print("[bold green3]Nombres de tours : [bold green3]"
                    f"[bold yellow]{tournament.number_of_rounds}[bold yellow]")

            c.print("[bold green3]Time control : [bold green3]"
                    f"[bold yellow]{tournament.time_control}[bold yellow]")

            c.print("[bold green3]Description : [bold green3]"
                    f"[bold yellow]{tournament.description}[bold yellow]")

            c.print("[bold green3]Liste des joueurs: [bold green3]")
            self.display_player_in_row(tournament_list)

            c.print("[bold green3]Liste des scores par joueurs: [bold green3]")
            self.display_player_score(tournament)

            c.print(f"[bold green3]Liste des tours :[bold green3]")
            RoundView().display_for_tournament(tournament)

    def report_display_tour_in_tournament(self, tournament_list):
        """
        This function used in report return each round in and tournament
        selected

        Args:
            tournament_list (list): list of each tournament instance created

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
            """
            round_list_to_display = []
            for round in round_list:

                if tournament_choosen.name in round.tournament_name:

                    round_list_to_display.append(round)
            """

        RoundView().display_for_tournament(tournament_choosen)

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

        MatchView().display_match_for_report(tournament_choosen)

    def display_report(self, secondary_menu, ):
        """
        This report function user all precedents functions and displayer user
        choice
        Args:
            tournament_list (list): list of each tournament instance created
            round_list (list): list of each round instance created in
            tournament
        """

        for element in secondary_menu:
            c.print(secondary_menu[element]["label"])
        menu_choice = c.input("[bold red]==> [bold red]")

        if menu_choice in secondary_menu:
            return secondary_menu[menu_choice]["action"]()
        c.print("\n[bold red]Merci de faire un choix présent"
                " dans le menu[bold red]\n")
