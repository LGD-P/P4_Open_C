from rich.console import Console
from datetime import datetime
import sys

from MODEL.tournament_model import Tournament
from MODEL.player_model import Player
from MODEL.match_model import Match

from VIEW.menu_view import MenuView
from VIEW.tournament_view import TournamentView
from VIEW.player_view import PlayerView

from CONTROLLER.player_controller import PlayerController
from CONTROLLER.tournament_controller import TournamentController


c = Console()


class MenuController:
    def __init__(self):
        self.running_program = True
        self.player_controller = PlayerController([])
        self.match_model = Match()
        self.tournament_controller = TournamentController(
            [], self.player_controller.player_list, [], self.match_model)
        self.menu_view_in_controller = MenuView({
            "1": {
                "label": "[bold blue]- 1. Créer des tournois :pencil: [bold blue]",
                "action": self.tournament_controller.add_tournament,
            },
            "2": {
                "label": "[bold blue]- 2. Créer des joueurs :pencil: [bold blue]",
                "action": self.player_controller.add_player,
            },
            "3": {
                "label": "[bold blue]- 3. Ajouter des joueurs à un tournois :pencil:[bold blue]",
                "action": self.tournament_controller.add_player_in_tournament,
            },
            "4": {
                "label": "[bold blue]- 4. Créer un Round :watch:[bold blue]",
                "action": self.tournament_controller.fill_round_instance_creat_announcement
            },
            "5": {
                "label": "[bold blue]- 5. Ajouter des résultats :trophy: [bold blue]",
                "action": self.tournament_controller.add_result,
            },
            "6": {
                "label": "[bold blue]- 6. Montrer le rapport :bar_chart: [bold blue]",
                "action": "",
            },
            "7": {
                "label": "[bold blue]- 7. Quitter :raising_hand: \n [bold blue]",
                "action": self.quit_menu,
            },

            "8": {
                "label": "[bold blue]- 8. Ajout rapide de tournois et joueurs \n"
                "[bold blue]",
                "action": self.generate_data
            }

        })

    def run_program(self):
        while self.running_program:
            self.menu_view_in_controller.display_menu_and_get_choice()

    def generate_data(self):

        quick_players_list = [
            Player("DENIS", "Laurent", "11-12-2000", "h", 321),
            Player("LAURENT", "Denis", "11-10-2005", "h", 123),
            Player("MOINE", "Alice", "10-10-1990", "f", 100),
            Player("VAULT", "Lise", "01-02-1980", "f", 10),
            Player("CREPIN", "Maurice", "12-07-1950", "h", 40),
            Player("TIAGO", "Daniela", "05-06-1977", "f", 35),
            Player("EDON", "Gabrielle", "09-03-1985", "f", 25),
            Player("PATTON", "Gabriel", "09-03-1970", "h", 20)]

        for players in quick_players_list:
            self.player_controller.player_list.append(players
                                                      )

        quick_tounarment = [
            Tournament("PARIS Chess-Event", "Paris",
                       datetime.now().strftime("%d-%m-%Y"),
                       [], quick_players_list[0:9], "Blitz",
                       "Description", 4, [])
        ]

        for tournnaments in quick_tounarment:
            self.tournament_controller.tournament_list.append(tournnaments)

        for tournament in quick_tounarment:
            for player in tournament.players:
                tournament.player_score.append(
                    {"player": player, "player_rank": player.rank, 'score': 0})

    def quit_menu(self):
        self.menu_view_in_controller.quit_message()
        self.running_program = False
