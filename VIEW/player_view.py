from rich.console import Console
from datetime import datetime

from MODEL.tournament_model import Tournament
from MODEL.player_model import Player

c = Console()


class PlayerView:

    def display_player_form(self):

        last_name = c.input(
            "[bold green3]Entrez le nom du Joueur: [bold green3] ")
        while last_name.isdigit():
            c.print("[bold red]\nInvalide, le nom ne peut pas contenir "
                    "de numéro\n ")
            last_name = c.input("[bold green3]Entrez le nom du Joueur:"
                                "[bold green3] ")

        first_name = c.input("[bold green3]Entrez le prénom du Joueur: "
                             "[bold green3] ")
        while first_name.isdigit():
            c.print("[bold red]\nInvalide, le prénom ne peut pas contenir "
                    "de numéro\n ")
            first_name = c.input("[bold green3]Entrez le prénom du Joueur:"
                                 "[bold green3] ")

        c.print("[bold green3]Entrez la date de naissance du joueur :")

        day = c.input("Jour: ")
        while not day.isdigit() or int(day) not in range(1, 32):
            c.print("[bold red]\nInvalide: entrez un jour entre 1 et 31")
            day = c.input("Jour: ")

        month = c.input("Mois: ")
        while not month.isdigit() or int(month) not in range(1, 13):
            c.print("[bold red]\nInvalide: entrez un jour entre 1 et 12")
            month = c.input("Mois: ")

        while int(month) == 2 and int(day) in range(29, 32):
            c.print("[bold red] Le mois de février ne compte pas de 29 30 "
                    "ou 31[bold red]")

            day = c.input("Jour: ")
            while not day.isdigit() or int(day) not in range(1, 32):
                c.print("[bold red]\nInvalide: entrez un jour entre 1 et 31")
                day = c.input("Jour: ")

            month = c.input("Mois: ")
            while not month.isdigit() or int(month) not in range(1, 13):
                c.print("[bold red]\nInvalide: entrez un jour entre 1 et 12")
                month = c.input("Mois: ")

        year = c.input("Année: ")
        while not year.isdigit() or not int(year) in range(
            (int(datetime.now().strftime("%Y"))-118),
                (int(datetime.now().strftime("%Y"))-10)):
            c.print("[bold red]\nInvalide: Le joueur doit avoir "
                    "au moins 10 ans, au plus 118 ans")
            year = c.input("Année: ")

        birth = (f'{day}-{month}-{year}')

        sex_list = ["h", "f"]
        sex = c.input("[bold green3]Entrez le sexe: H - F[bold green3] ")
        while not sex.lower() in sex_list or sex.isdigit():
            c.print("[bold red]\nInvalide ")
            sex = c.input("[bold green3]Entrez le sexe du joueur: H / F "
                          "[bold green3]")

        rank = c.input("[bold green3]Entrez le classement du joueur:"
                       "[bold green3]")

        created_player = Player(last_name, first_name,
                                str(birth), sex, int(rank), 0)

        return created_player

    def display_players_to_choose(self, player_list, tourament_list):
        if player_list:
            c.print("[bold yellow] Liste des joueurs disponibles:\n[bold yellow]")

            for player in player_list:
                if not player in tourament_list:
                    c.print(
                        f"- {player_list.index(player)} [bold green] {player.last_name} {player.first_name} {player.rank}[bold green]")
                else:
                    pass
                    """c.print(f"- {player_list.index(player)}  {player} [bold red]joueur DEJA DANS LE"
                            "TOURNOIS[bold red]")"""

        """
       counter = -1
        value = []
        key = []
        c.print("[bold yellow] Liste des joueurs disponibles:\n[bold yellow]")
        if player_list:
            for global_player in player_list:
                if not global_player in tourament_list:
                    value.append(
                        f"{global_player.last_name}  {global_player.first_name}  classement = {global_player.rank}")
                else:
                    c.print(
                        "[bold red]Pas de joueurs disponibles dans la liste, pour ce tournois...[bold red]")

            for _ in range(len(value)):
                counter += 1
                key.append(counter)

            players_availables = dict(zip(key, value))

            for k, v in players_availables.items():
                c.print(f"[bold blue]- {k}: {v}[bold blue]\n")

            return players_availables

        else:
            c.print("[bold red]Aucun joueurs n'a été créé...[bold red]")
"""
