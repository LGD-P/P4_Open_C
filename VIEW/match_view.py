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

                else:
                    match_index = -1
                    for match in tournament.tours:
                        match_index += 1
                        c.print("\n==========================\n")
                        c.print(
                            f"- Dans le tournois {tournament.name:}\n"
                            f"  Qui a gagné ce match : {match[match_index][0].last_name}"
                            f" {match[match_index][0].first_name} contre "
                            f"{match[match_index][1].last_name} "
                            f"{match[match_index][1].first_name}\n"
                            f"- 1: {match[match_index][0].last_name}\n"
                            f"- 2: {match[match_index][1].last_name}\n"
                            f"- 3: Egalité\n"
                        )

                        winner = c.input(
                            "[bold red]Entrez le vainqueur : [bold red]")
