from rich.console import Console
from rich.table import Table
from rich import inspect
from datetime import datetime
c = Console()


class RoundView:

    def display_round_view(self, tournament_running):
        """This funciton display a dashboard with matchs anouncements

        Args:
            tournament_running (list): match in tournament running

        Returns:
            None : none if no tournament is running
        """

        if not tournament_running:
            return None
        else:

            table = Table(
                title=f"",
                style="red")

            table.add_column("Joueur Un", justify="center",
                             style="cyan", no_wrap=True)
            table.add_column(
                "Jouera contre", justify="center", style="magenta")
            table.add_column("Joueur Deux", justify="center", style="green")

            index = -1
            # for tournament in tournament_list:
            """
            if type(tournament_running.tours[-1]) == dict:
                for players_match in tournament_running.tours[-1]['match_list']:

                    index += 1
                    table.add_row(
                        f"\n{players_match[0][0]} "
                        f"Score  : {players_match[0][1]}\n",
                        "\n== Jouera contre == >\n",
                        f"\n{players_match[1][0]} "
                        f"Score : {players_match[1][1]}\n",
                        end_section=True)

                c.print(table)

            else:
            """
            for players_match in tournament_running.tours[-1].match_list:

                index += 1
                table.add_row(
                    f"\n{players_match[0][0]} "
                    f"Score  : {players_match[0][1]}\n",
                    "\n== Jouera contre == >\n",
                    f"\n{players_match[1][0]} "
                    f"Score : {players_match[1][1]}\n",
                    end_section=True)

            c.print(table)

    def debug_print(self, tournament):

        for round in tournament.tours:
            if round.ending_hour == None:
                c.print(
                    f"{round.tournament_name}\n"
                    f"{round.name}\n"
                    f"Commencé le :"
                    f"{round.starting_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n"
                    f"Pas encore terminé\n"
                    f"{round.number_of_round}\n"
                    f"{round.match_list}\n")
            else:
                c.print(
                    f"{round.tournament_name}\n"
                    f"{round.name}\n"
                    f"Commencé le :"
                    f"{round.starting_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n"
                    f"Terminé le :"
                    f"{round.ending_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n"
                    f"{round.number_of_round}\n"
                    f"{round.match_list}\n")

    def display_for_tournament(self, tournament):
        for round in tournament.tours:

            """
            if type(round) == dict:

                if not round["ending_hour"]:
                    c.print(
                        f"[bold yellow]- Round N°{tournament.tours.index(round) + 1 }[bold yellow]\n")
                    c.print(
                        f"Commencé le :"
                        f"{datetime.strptime(round['starting_hour'][0:19], '%Y-%m-%d  %H:%M:%S')}\n")
                    self.display_round_view(tournament)
                    c.print(f"Ce round n'est pas encore terminé\n")

                else:
                    c.print(
                        f"[bold yellow]- Round N°{tournament.tours.index(round) + 1}[bold yellow]\n")
                    c.print(
                        f"Commencé le :"
                        f"{datetime.strptime(round['starting_hour'][0:19], '%Y-%m-%d  %H:%M:%S')}\n")
                    self.display_round_view(tournament)
                    c.print(f"Terminé le :"
                            f"{datetime.strptime(round['ending_hour'][0:19], '%Y-%m-%d  %H:%M:%S')}\n")
            else:
            """
            if not round.ending_hour:
                c.print(
                    f"[bold yellow]- Round N°{tournament.tours.index(round) + 1}[bold yellow]\n")
                c.print(
                    f"Commencé le :"
                    f"{round.starting_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n")
                self.display_round_view(tournament)
                c.print(f"Ce round n'est pas encore terminé\n")

            else:
                c.print(
                    f"[bold yellow]- Round N°{tournament.tours.index(round) + 1}[bold yellow]\n")
                c.print(f"Commencé le :"
                        f"{round.starting_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n")
                self.display_round_view(tournament)
                c.print(f"Terminé le :"
                        f"{round.ending_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n")
