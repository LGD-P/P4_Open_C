from rich.console import Console
from rich.table import Table
from rich import inspect
from datetime import datetime
c = Console()


class RoundView:

    def display_launching_round_view(self, tournament_running):
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

            for players_match in tournament_running.tours[-1].match_list:

                index += 1
                table.add_row(
                    f"\n{players_match[0][0].last_name} {players_match[0][0].first_name}\n "
                    f"Score  : {players_match[0][1]}\n",
                    "\n== Jouera contre == >\n",
                    f"\n{players_match[1][0].last_name} {players_match[1][0].first_name}\n "
                    f"Score : {players_match[1][1]}\n",
                    end_section=True)

            c.print(table)

    def display_round_view_for_report(self, round):
        """This funciton display a dashboard with matchs anouncements

        Args:
            tournament_running (list): match in tournament running

        Returns:
            None : none if no tournament is running
        """

        table = Table(
            title=f"",
            style="red")

        table.add_column("Joueur Un", justify="center",
                         style="cyan", no_wrap=True)
        table.add_column(
            "A joué contre", justify="center", style="magenta")
        table.add_column("Joueur Deux", justify="center", style="green")

        # for tournament in tournament_list:
        for players in round:
            table.add_row(
                f"\n{players[0][0].last_name} {players[0][0].first_name}\n "
                f"Score  : {players[0][1]}\n",
                "\n== A joué contre == >\n",
                f"\n{players[1][0].last_name} {players[1][0].first_name}\n "
                f"Score : {players[1][1]}\n",
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

            if not round.ending_hour:
                c.print(
                    f"[bold yellow]- Round "
                    f"N°{tournament.tours.index(round) + 1}[bold yellow]\n")
                c.print(
                    f"Commencé le :"
                    f"{round.starting_hour.strftime('%d-%m-%Y - %H:%M:%S')}"
                    "\n")
                self.display_round_view_for_report(round.match_list)
                c.print(f"Ce round n'est pas encore terminé\n")

            else:
                c.print(
                    f"[bold yellow]- Round "
                    f"N°{tournament.tours.index(round) + 1}[bold yellow]"
                    "\n")
                c.print(
                    f"Commencé le :"
                    f"{round.starting_hour.strftime('%d-%m-%Y - %H:%M:%S')}"
                    "\n")
                self.display_round_view_for_report(round.match_list)
                c.print(
                    f"Terminé le :"
                    f"{round.ending_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n")
