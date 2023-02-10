from rich.console import Console


c = Console()


class MatchView:
    def display_tournament_to_fill_result(self, started_tournaments,
                                          tournament_list):
        """This function display tournament available to receive players_score

        Args:
            started_tournaments (list): list of tournament already launch
            tournament_list (list): list of tournament regesitered

        Returns:
            instance: tournament choosen
        """

        if not started_tournaments:
            c.print(
                "[bold red]Il faut d'abord créer et commencer "
                "un tournois[bold red]"
            )
            pass

        else:

            for tournament in started_tournaments:
                choice_list = []

                choice_list = [started_tournaments.index(tournament)]

            c.print("[bold yellow]A Quel tournois voulez-vous ajouter "
                    "des résultats ?[bold yellow]\n\n"
                    f"- {started_tournaments.index(tournament)} : "
                    f"[bold green]{tournament.name}[bold green]\n")

            tournament_choice = c.input("==> ")

            while not tournament_choice.isdigit() \
                    or not int(tournament_choice) in choice_list:
                c.print(
                    '[bold red] Merci de faire un choix dans "\
                        "la liste[bold red]')
                tournament_choice = c.input("==> ")

            # c.print(started_tournaments[int(tournament_choice)])
            tournament_choice = started_tournaments[int(
                tournament_choice)]

            if tournament_choice in tournament_list:
                tournament_choice = tournament_list[tournament_list.index(
                    tournament_choice)
                ]

            return tournament_choice

    def display_player_in_tournament_to_fill_score(self, tournament_choice,
                                                   match_list):
        """This function display players matchs and option to give
        players points

        Args:
            started_choice (instance): tournament choosen
            match_list (list): match in tournament choosen

        Returns:
            int: winner choosen
        """

        # tournament_list[started_tournaments[int(tournament_choice)]]

        c.print(
            f"- Dans le tournois {tournament_choice.name:}\n"
            f"  Qui a gagné ce match : "
            f"{match_list[0][1]}\n"
            f"- 0: {match_list[0][0]}\n"
            f"- 1: {match_list[0][1]}\n"
            f"- 2: Egalité\n"
        )

        winner = c.input(
            "[bold red]Entrez le vainqueur : [bold red]\n")

        while not winner.isdigit() or not int(winner) in [0, 1, 2]:
            winner = c.input(
                "[bold red] Faites un choix valide : 1, 2 ou 3 [bold red]\n")

        return winner

    def display_match_for_report(self, unique_match_list: list):

        while not unique_match_list:
            return c.print("[bold red]Il n'y a pas encore de match dans "
                           "la liste[bold red]")

        c.print("[bold magenta]Voici la liste matchs pour lesquels un score a"
                "été ajouté : \n[bold magenta]")
        index = 0
        for joueur in unique_match_list.match:
            index += 1
            c.print(f"[bold red]- Match N°{index}[bold red] ")
            c.print(
                "[bold cyan]Joueur :\n [bold cyan]"
                f"{joueur[0][0]}, "
                f"Score : "
                f"{joueur[0][1]},\n\n"
                "    == Contre ==>    \n\n"
                f"Joueur : "
                f"{joueur[1][0]}, "
                f"Score :\n[bold cyan] "
                f"{joueur[1][1]}\n")
