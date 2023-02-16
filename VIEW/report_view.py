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

            c.print("[bold magenta]Voici la liste des joueurs par rang:"
                    "\n[bold magenta]")
            for player in sorted_players:
                c.print(player)

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

        RoundView().debug_print(round_list_to_display)

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

            MatchView().display_match_for_report(tournament_choosen.tours)

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
