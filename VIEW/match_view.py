from rich.console import Console
from collections import defaultdict

c = Console()


class MatchView:
    def display_match_to_add_result(self, started_tournaments, tournament_list):
        # result = defaultdict(int, {})
        # result = round_list[-1]

        # c.print(started_tournaments)

        if not started_tournaments:
            c.print(
                "[bold red]Il faut d'abord créer et commencer "
                "un tournois[bold red]"
            )
            pass

        else:

            for tournament in started_tournaments:

                choice_list = [started_tournaments.index(tournament)]

                c.print("[bold yellow]A Quel tournois voulez-vous ajouter "
                        "des résultats ?[bold yellow]\n\n"
                        f"- {started_tournaments.index(tournament)} : [bold green]{tournament.name}[bold green]\n")
                tournament_choice = c.input("==> ")

                while not tournament_choice.isdigit() or not int(tournament_choice) in choice_list:
                    c.print(
                        '[bold red] Merci de faire un choix dans la liste[bold red]')
                    tournament_choice = c.input("==> ")

            # c.print(started_tournaments[int(tournament_choice)])
            tournament_choice = started_tournaments[int(
                tournament_choice)]

            if tournament_choice in tournament_list:
                tournament_choice = tournament_list[tournament_list.index(
                    tournament_choice)
                ]

                # tournament_list[started_tournaments[int(tournament_choice)]]

            round_index = (len(tournament_choice.tours))
            round = tournament_choice.tours[round_index - 1]

            index = -1
            for match_list in round:
                index += 1
                c.print(
                    f"- Dans le tournois {tournament_choice.name:}\n"
                    f"  Qui a gagné ce match : {match_list[0]['player'].last_name} "
                    f"{match_list[0]['player'].first_name} contre "
                    f"{match_list[1]['player'].last_name} "
                    f"{match_list[1]['player'].first_name}\n"
                    f"- 0: {match_list[0]['player'].last_name}\n"
                    f"- 1: {match_list[1]['player'].last_name}\n"
                    f"- 2: Egalité\n"
                )

                winner = c.input(
                    "[bold red]Entrez le vainqueur : [bold red]\n")

                while not winner.isdigit() or not int(winner) in [0, 1, 2]:
                    winner = c.input(
                        "[bold red] Faites un choix valide : 1, 2 ou 3 [bold red]\n")

                if int(winner) == 2:
                    for player in tournament_choice.player_score:
                        if player["player"] == match_list[0]['player']:
                            player["score"] += 0.5
                        elif player["player"] == match_list[1]['player']:
                            player["score"] += 0.5

                elif int(winner) == 0:
                    for player in tournament_choice.player_score:
                        if player["player"] == match_list[0]['player']:
                            player["score"] += 1
                        elif player["player"] == match_list[1]['player']:
                            player["score"] += 0

                elif int(winner) == 1:
                    for player in tournament_choice.player_score:
                        if player["player"] == match_list[0]['player']:
                            player["score"] += 0
                        elif player["player"] == match_list[1]['player']:
                            player["score"] += 1
