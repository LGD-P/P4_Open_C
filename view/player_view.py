from rich.console import Console
from datetime import datetime


c = Console()


class PlayerView:

    def display_player_form(self):
        """This function display form to creat a player

        Returns:
            dict: {"attribute" : user entry}
        """

        last_name = c.input(
            "[bold green3]Entrez le nom du Joueur: [bold green3] ")
        while last_name.isdigit():
            c.print("[bold red]\nInvalide, le nom ne peut pas contenir de numéro\n ")
            last_name = c.input("[bold green3]Entrez le nom du Joueur:[bold green3] ")

        first_name = c.input("[bold green3]Entrez le prénom du Joueur: [bold green3] ")
        while first_name.isdigit():
            c.print("[bold red]\nInvalide, le prénom ne peut pas contenir de numéro\n ")
            first_name = c.input("[bold green3]Entrez le prénom du Joueur:[bold green3] ")

        birth = self.birthform()

        sex_list = ["h", "f"]
        sex = c.input("[bold green3]Entrez le sexe: H - F[bold green3] ")
        while not sex.lower() in sex_list or sex.isdigit():
            c.print("[bold red]\nInvalide ")
            sex = c.input("[bold green3]Entrez le sexe du joueur: H / F [bold green3]")

        rank = c.input("[bold green3]Entrez le classement du joueur:[bold green3]")

        return {
            "last_name": last_name,
            "first_name": first_name,
            "birth": birth,
            "sex": sex,
            "rank": rank
        }

    def display_players_to_choose(self, player_list, tournament):
        """This function display players availables in global list to fill
        tournament with. If a player already is in tournament he will not
        be display.

        Args:
            player_list (list): _players list
            tournament_list (list): tournament list
        """

        player_available = []
        unique_player_available = []
        if player_list:
            c.print("[bold yellow] Liste des joueurs disponibles:\n"
                    "[bold yellow]")

            for player in player_list:
                if player not in tournament.players:
                    player_available.append(player)

            [unique_player_available.append(
                player) for player in player_available if player not in unique_player_available]

            for player in unique_player_available:
                if player not in tournament.players:
                    c.print(
                        f"- {player_list.index(player)} [bold green] "
                        f"{player.last_name}"
                        f" {player.first_name}, rang :  "
                        f"{player.rank}[bold green]")

    def birthform(self):
        """This function display form to get bith
        check with datetiume if date really exist

        Returns:
            datetime : d% m% Y%
        """
        print("Entez la date de naissance du joueur")
        exist = False
        while exist is False:
            year = input("Année: ")
            while not year.isdigit() or int(year) not in range(
                (int(datetime.now().strftime("%Y")) - 118),
                    (int(datetime.now().strftime("%Y")) - 10)):
                c.print("[bold red]\nInvalide: Le joueur doit avoir au moins 10 ans, au plus 118 ans[bold red]")
                year = c.input("Année: ")

            month = input("Mois ")
            while not month.isdigit() or int(month) not in range(1, 13):
                c.print("[bold red]\nInvalide: entrez un jour entre 1 et 12[bold red]")
                month = c.input("Mois: ")

            day = input("Jour ")
            while not day.isdigit() or int(day) not in range(1, 32):
                c.print("[bold red]\nInvalide: entrez un jour entre 1 et 31[bold red]")
                day = c.input("Jour: ")

            try:
                birth = f"{day}/{month}/{year}"
                birth = datetime.strptime(birth, "%d/%m/%Y")
                exist = True
                return birth

            except ValueError:
                c.print("[bold red]La date entrée n'est pas correcte[bold red]")
