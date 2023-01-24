from rich.console import Console

c = Console()


class MatchView:
    def display_match_to_add_result(self, started_tournaments, tournament_list):
        result = {}

        for tournament in started_tournaments:
            for player in tournament.players:
                tournament.player_score[f"{player}"] = 0

        c.print(started_tournaments)

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
                        f"- {index} : [bold green]{tournament.name}[bold green]\n")
                tournament_choice = c.input("==> ")

                # prévoir les condition en cas de choix hors liste :

                # à prévoir la modification des instances de tournois concernés par les résultats

                # c.print(started_tournaments[int(tournament_choice)])
                tournament_choice = started_tournaments[int(tournament_choice)]

                if tournament_choice in tournament_list:
                    tournament_choice = tournament_list[tournament_list.index(
                        tournament_choice)
                    ]

                # tournament_list[started_tournaments[int(tournament_choice)]]

                round = tournament_choice.tours
                index = -1
                for match_list in round:
                    for _ in match_list:
                        index += 1

                        c.print(
                            f"- Dans le tournois {tournament_choice.name:}\n"
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
                            result[f"{match_list[index][0]}"] += 0.5
                            result[f"{match_list[index][1]}"] += 0.5

                        elif int(winner) == 0:
                            result[f"{match_list[index][0]}"] += 0
                            result[f"{match_list[index][1]}"] += 1
                        elif int(winner) == 1:
                            result[f"{match_list[index][0]}"] += 1
                            result[f"{match_list[index][1]}"] += 0

                    return result
