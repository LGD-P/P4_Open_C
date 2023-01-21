from rich.console import Console

c = Console()


class MatchView:
    def display_match_to_add_result(self, started_tournaments, tournament_list):
        if not started_tournaments:
            c.print(
                "[bold red]Il faut d'abord créer et commencer "
                "un tournois[bold red]"
            )
            pass
        else:
            index = -1
            for tournament in started_tournaments:
                index += 1
                c.print("[bold yellow]A Quel tournois voulez-vous ajouter "
                        "des résultats ?[bold yellow]\n\n"
                        f"[bold green]- {index} : {tournament.name}[bold green]\n")
                tournament_choice = c.input("==> ")

                # à prévoir la modification des instances de tournois concernés par les résultats
                started_tournaments[int(tournament_choice)]
                # prévilégier l'appel direct à la tournament liste
                tournament_list[started_tournaments[int(tournament_choice)]]

                """
                index = -1
                for tournament in tournament_list:
                    for match_list in tournament.tours:
                        for _ in match_list:
                            index += 1
                            # problème d'affichage...
                            c.print(
                                f"- Dans le tournois {tournament.name:}\n"
                                f"  Qui a gagné ce match : {match_list[index][0].last_name} "
                                f"{match_list[index][0].first_name} contre "
                                f"{match_list[index][1].last_name} "
                                f"{match_list[index][1].first_name}\n"
                                f"- 0: {match_list[index][0].last_name}\n"
                                f"- 1: {match_list[index][1].last_name}\n"
                                f"- 2: Egalité\n"
                            )

                            winner = c.input(
                                "[bold red]Entrez le vainqueur : [bold red]\n")

                            while not winner.isdigit() or not int(winner) in [0, 1, 2]:
                                winner = c.input(
                                    "[bold red] Faites un choix valide : 1, 2 ou 3 [bold red]\n")

                            if int(winner) == 2:
                                winner = 0.5
                            elif winner == 0:
                                winner = 0
                            elif winner == 1:
                                winner = 1

                            return winner
                            """
