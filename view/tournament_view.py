
from rich.console import Console
from rich.table import Table
from datetime import datetime


c = Console()


class TournamentView:

    def display_add_tournament_form(self):
        """
        This function take user input to fill player settings

        Returns:
            dict : {'player attributes' : user input}
        """
        name = c.input("[bold green3]Entrez le nom du Tournois : [bold green3] ")
        date = datetime.now()
        place = c.input("[bold green3]Entrez le lieu du Tournois [bold green3] ")
        tours = []
        players = []
        time_control_dict = {1: "Bullet", 2: "Blitz", 3: "Coup rapide"}

        time_control = c.input("[bold green3]Choisissez le mode de contrôle du temps\n[bold green3]"
                               "[bold green]- 1. Bullet\n"
                               "- 2. Blitz\n"
                               "- 3. Coup rapide\n[bold green]")

        while not time_control.isdigit() or int(time_control) <= 0 \
                or int(time_control) > 3:
            c.print("[bold red]\nInvalide, possiblités ==> 1. 2. 3. [bold red]\n")
            time_control = input(
                "- 1. Bullet\n"
                "- 2. Blitz\n"
                "- 3. Coup rapide\n"
            )

        time_control = time_control_dict[int(time_control)]

        description = c.input("[bold green3]Indiquez la description du tournois [bold green3]")
        c.print("\n[bold red]Tournois ajouté 👍 [bold red]")

        return {
            "name": name,
            "date": date,
            "place": place,
            "tours": tours,
            "players": players,
            "time_control": time_control,
            "description": description,
            "player_score": {}
        }

    def display_tournament_to_fill(self, tournament_list, player_list):
        """
        This function display tournament available
        User choose one and can fill it with players

        Args:
            tournament_list (list): list of each tournament instance created

        Returns:
            instance: tournament
        """
        choice_tournament_available = []
        if tournament_list:
            for tournament in tournament_list:
                if len(tournament.tours) == 0\
                        and not len(tournament_list[tournament_list.index(tournament)].players) == len(player_list):
                    choice_tournament_available.append(
                        tournament_list.index(tournament))
                # if not len(tournament.players) % 2:

            while choice_tournament_available == []:
                c.print((
                    "[bold red]- 1 Soit vous n'avez pas encore de créer de tournois "
                        "des joueurs\n - 2 Soit le tournois contient déjà tous les joueurs enregistrés.[bold red]"
                        ))
                return None

            for tournament in choice_tournament_available:
                c.print(f"{tournament} [bold green]"
                        f"{tournament_list[tournament].name},"
                        f"{tournament_list[tournament].place}[bold green]\n")

            tournament_choice = c.input(
                "[bold blue]Faites votre choix :  [bold blue]"
            )

            c.print("[bold blue]Choisissez un tournois dans lequel"
                    " ajouter un joueur: [bold blue]\n"
                    )
            while not tournament_choice.isdigit() or not \
                    int(tournament_choice) in choice_tournament_available:
                tournament_choice = c.input(
                    "[bold red]Veillez faire un choix dans la liste[bold red]"
                )

            # retourner directement l'instance du tournois
            return tournament_list[int(tournament_choice)]

    def display_add_player_in_tournament_form(self, tournament_list, player_list, player_view):
        """
        This function display only players available to fill tournament with
        returning a dict with tournament and player choosen

        Args:
            tournament_list (list): list of each tournament instance created
            player_view (instance): view instance to use player_view method
            and display player tournament_list (list): list of each player
            instance created

        Returns:
            dict: {
                    "chosen_tournament": tournament instance ,
                    "chosen_player": player instance
                }
        """
        if not tournament_list:
            c.print("[bold red]Veuillez créer un tournois pour pouvoir l'alimenter en joueurs..\n [bold red]")
            return None

        elif not player_list:
            c.print("[bold red]Veuillez créer des joueurs pour pouvoir les ajouter à des tournois")
            return None

        else:
            tournament = self.display_tournament_to_fill(tournament_list, player_list)
            if not tournament:
                return None
            else:

                player_view.display_players_to_choose(
                    player_list, tournament)

                player_choice = c.input("[bold yellow]Choisissez votre joueur\n ==> [bold yellow]")
                choice_list = []
                for player in player_list:
                    choice_list.append(player_list.index(player))

                while not player_choice.isdigit() \
                        or int(player_choice) not in choice_list:
                    c.print("[bold red]Faites un choix parmis ceux disponibles[bold red]")
                    player_choice = c.input("[bold yellow]==> [bold yellow]")

                while player_list[int(player_choice)] in tournament.players:
                    c.print("[bold red]Ce joueur est déjà dans la liste [bold red]")
                    player_choice = c.input("[bold yellow]==> [bold yellow]")

                return {
                    "chosen_tournament": tournament,
                    "chosen_player": player_list[int(player_choice)]
                }

    def display_choose_a_tournament_to_launch(self, tournament_list):
        """
        This function check the tournament list and propose user to launch one

        Args:
            tournament_list (list): list of each tournament instance created

        Returns:
            instance: tournament instance
        """
        if tournament_list:
            tournament_available = []

            for tournament in tournament_list:
                if len(tournament.players) == 0 or len(tournament.players) % 2 == 1:
                    continue
                try:
                    if len(tournament.tours) > 0 and tournament.tours[-1].ending_hour is None:
                        continue
                except TypeError:
                    tournament.tours = []
                    tournament_available.append(tournament)
                    continue

                tournament_available.append(tournament)

            if len(tournament_available) == 0:
                c.print("[bold red]Votre tournois est déjà en cours veuillez remplir les scores[bold red]")
                return None
            else:
                for tournament in tournament_available:
                    c.print(
                        f"{tournament_available.index(tournament)} [bold green]"
                        f"{tournament.name}, {tournament.place}"
                        "[bold green]\n")

            tournament_choice = c.input("[bold blue]Faites votre choix :  [bold blue]")

            choice_player = []
            index = -1
            for _ in tournament_available:
                index += 1
                choice_player.append(index)

            while not tournament_choice.isdigit() or not \
                    int(tournament_choice) in choice_player:
                c.print("[bold red] Merci de faire un choix dans la liste[bold red]")
                tournament_choice = c.input("==> ")

            tournament_to_launch = tournament_available[int(
                tournament_choice)]

            return tournament_to_launch

        else:
            c.print("[bold red]Vous devez créer un tournois d'abord...\n[bold red]")
            return None

    def display_winner(self, player: list, player_score):

        table = Table(title="", style="red")

        table.add_column(
            "[bold red]:1st_place_medal: Et le Vainqueur est : :1st_place_medal:[bold red]",
            justify="center", style="cyan",
            no_wrap=True,)

        table.add_row(
            f"{player.last_name} {player.first_name}"
            f" avec un score de {player_score}")

        c.print(table)
