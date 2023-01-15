from rich.console import Console
c = Console()


class RoundView:

    def display_round_view(self, first_list_of_round):
        index = -1
        for _ in first_list_of_round:
            index += 1
            c.print(
                f"{first_list_of_round[index][0].last_name} jouera contre "
                f"{first_list_of_round[index][1].last_name}")
            c.print('[bold red]***************\n[bold red]')
