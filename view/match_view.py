from rich.console import Console
from rich.table import Table
# from rich import inspect

c = Console()


class MatchView:
    def display_tournament_to_fill_result(self, tournament_list):
        """This function display tournament available to receive players_score

        Args:
            tournament_list (list): list of tournament registered

        Returns:
            instance: tournament chose
        """

        started_tournaments = [t for t in tournament_list if len(
            t.tours) > 0 and t.tours[-1].ending_hour is None]
        if not started_tournaments:
            c.print(
                "[bold red]Il faut d'abord créer et commencer un tournois[bold red]")
            return None

        else:
            choice_list = {str(index): tournament for index, tournament in enumerate(started_tournaments)}

            c.print("[bold yellow]A quel tournois voulez-vous ajouter des résultats ?[bold yellow]\n\n")
            for index, tournament in choice_list.items():
                c.print(f"- {index} : [bold green]{tournament.name}[bold green]\n")

            tournament_choice = c.input("==> ")

            while tournament_choice not in choice_list:
                c.print("[bold red] Merci de faire un choix dans la liste[bold red]")
                tournament_choice = c.input("==> ")

            return choice_list[tournament_choice]

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

        c.print(
            f"- Dans le tournois {tournament_choice.name:}\n"
            f"  Qui a gagné ce match : \n"
            f"- 0: {match_list[0][0].last_name} {match_list[0][0].first_name}\n"
            f"- 1: {match_list[1][0].last_name} {match_list[1][0].first_name}\n"
            f"- 2: Egalité\n"
        )

        winner = c.input("[bold red]Entrez le vainqueur : [bold red]\n")

        while not winner.isdigit() or not int(winner) in [0, 1, 2]:
            winner = c.input("[bold red] Faites un choix valide : 1, 2 ou 3 [bold red]\n")

        return winner

    def display_match_for_report(self, tournament):

        if not tournament:
            return c.print("[bold red]Il n'y a pas encore de match dans la liste[bold red]")

        index_round = 0

        for round in tournament.tours:

            index_round += 1

            table = Table(title=f'[bold red]- Matchs dans le Round '
                          f'N°{index_round}[bold red]',
                          show_lines=True, style="green3")

            table.add_column("[bold yellow1]Joueur 1:[bold yellow1]", justify="center", no_wrap=True)
            table.add_column("[bold red] ===CONTRE===> [bold red]", justify="center", style="red", no_wrap=True)
            table.add_column("[bold yellow1]Joueur 2:[bold yellow1]", justify="center", no_wrap=True)

            for match in round.match_list:

                table.add_row(f"[bold cyan]"
                              f"{match[0][0].last_name} {match[0][0].first_name},\n "
                              f"Score : "
                              f"{match[0][1]},\n",
                              "\n== Contre ==>\n",
                              f"[bold cyan]"
                              f"{match[1][0].last_name} {match[1][0].first_name},\n "
                              f"Score : [bold cyan] "
                              f"{match[1][1]}\n")
            c.print(table)
