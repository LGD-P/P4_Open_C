from rich.console import Console
from rich.table import Table
c = Console()


class RoundView:

    def display_round_view(self, tournament_running):

        if tournament_running == None:
            return None
        else:
            table = Table(
                title="[bold yellow]-Premier Round du tournois-[bold yellow]", style="red")

            table.add_column("Joueur Un", justify="center",
                             style="cyan", no_wrap=True)
            table.add_column(
                "Jouera contre", justify="center", style="magenta")
            table.add_column("Joueur Deux", justify="center", style="green")

            index = -1
            # for tournament in tournament_list:
            for players_match in tournament_running.tours[-1]:
                index += 1
                table.add_row(
                    f"\n{players_match[0].last_name} "
                    f"{players_match[0].first_name}\n"
                    f"classement : {players_match[0].rank}\n",
                    f"\n== Jouera contre == >\n",
                    f"\n{players_match[1].last_name} "
                    f"{players_match[1].first_name}\n"
                    f"classement : {players_match[1].rank}\n",
                    end_section=True)

            c.print(table)

    def debug_print(self, round_list):
        for round in round_list:
            if round.ending_hour == None:
                c.print(f"{round.tournament_name}\n"
                        f"{round.name}\n"
                        f"{round.starting_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n"
                        f"{None}\n"
                        f"{round.number_of_round}\n"
                        f"{round.match_list}\n")
            else:
                c.print(f"{round.tournament_name}\n"
                        f"{round.name}\n"
                        f"{round.starting_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n"
                        f"{round.ending_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n"
                        f"{round.number_of_round}\n"
                        f"{round.match_list}\n")

    # Prévoir l'affichage des points dans le tableau avec un self.tournament pour
    # le player score
    # f"scrore : {tournament.player_score[f'{first_round_list[index][0].last_name}']}
    # {tournament.player_score[f'{first_round_list[index][0].first_name}']} "
