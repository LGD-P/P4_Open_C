from rich.console import Console


from VIEW.tournament_view import TournamentView
from VIEW.player_view import PlayerView


c = Console()


class TournamentController:
    def __init__(self, tournament_list, player_list):
        self.tournament_view = TournamentView()
        self.tournament_list = tournament_list
        self.player_view = PlayerView()
        self.player_list = player_list

    def add_tournament(self):
        self.tournament_list.append(
            self.tournament_view.display_add_tournament_form())
        # prin de débug
        print(self.tournament_list)

    def add_player_in_tournament(self):
        self.tournament_view.display_add_player_in_tournament_form(
            self.tournament_list, self.player_list)
