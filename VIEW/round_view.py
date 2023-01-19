from rich.console import Console
from rich.table import Table
c = Console()


class RoundView:

    def display_round_view(self, first_round_list):
        if not first_round_list:
            pass
        else:
            table = Table(
                title="[bold yellow]-Premier Round du tournois-[bold yellow]", style="red")

            table.add_column("Joueur Un", justify="center",
                             style="cyan", no_wrap=True)
            table.add_column(
                "Jouera contre", justify="center", style="magenta")
            table.add_column("Joueur Deux", justify="center", style="green")

            index = -1
            for _ in first_round_list:
                index += 1
                table.add_row(
                    f"\n{first_round_list[index][0].last_name} "
                    f"{first_round_list[index][0].first_name}\n"
                    f"classement : {first_round_list[index][0].rank}\n"
                    f"points : {first_round_list[index][0].points}\n",
                    f"\n== Jouera contre == >\n",
                    f"\n{first_round_list[index][1].last_name} "
                    f"{first_round_list[index][1].first_name}\n"
                    f"classement : {first_round_list[index][1].rank}\n"
                    f"points : {first_round_list[index][1].points}\n",
                    end_section=True)

            c.print(table)
