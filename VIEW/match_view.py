from rich.console import Console

c = Console()


class MatchView:
    def display_match_to_add_result(self, tournament_list):
        if not tournament_list:
            c.print(
                "[bold red]Il faut d'abord créer un tournois[bold red]"
            )
            pass

        else:
            for tournament in tournament_list:
                if not tournament.tours:
                    c.print(

                        f"- {tournament.name} : [bold red]Le tournois n'a pas commencé\n"
                        " Il faut d'abord lancer le tournois[bold red]\n"
                    )
                    pass

        for tournament in tournament_list:
            for match_list in tournament.tours:
                for match in match_list:

                    c.print(
                        f"- Dans le tournois {tournament.name:}\n"
                        f"  Qui a gagné ce match : {match[0].last_name}"
                        f" {match[0].first_name} contre "
                        f"{match[1].last_name} "
                        f"{match[1].first_name}\n"
                        f"- 1: {match[0].last_name}\n"
                        f"- 2: {match[1].last_name}\n"
                        f"- 3: Egalité\n"
                    )

                    winner = c.input(
                        "[bold red]Entrez le vainqueur : [bold red]\n")

                    while not winner.isdigit() or not int(winner) in [1, 2, 3]:
                        winner = c.input(
                            "[bold red] Faites un choix valide : 1, 2 ou 3 [bold red]\n")

                    return winner
