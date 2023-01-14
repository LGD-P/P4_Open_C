from rich.console import Console


from VIEW.tournament_view import TournamentView
from VIEW.player_view import PlayerView
from MODEL.tournament_model import Tournament


c = Console()


class TournamentController:
    def __init__(self, tournament_list, player_list):
        self.tournament_view = TournamentView()
        self.tournament_list = tournament_list
        self.player_view = PlayerView()
        self.player_list = player_list

    def add_tournament(self):

        tournament = self.tournament_view.display_add_tournament_form()

        self.tournament_list.append(Tournament(tournament["name"], tournament["place"],
                                    tournament["date"], tournament["tours"],
                                    tournament["players"], tournament["time_control"],
                                    tournament["description"]))
        # print de débug
        c.print(self.tournament_list)

    def add_player_in_tournament(self):

        player_in_tournament = self.tournament_view.display_add_player_in_tournament_form(
            self.tournament_list, self.player_list)

        return player_in_tournament["chosen_tournament"].players.append(
            player_in_tournament["chosen_player"])

        # print de débug
        # print("PLAYER STOCKES DANS LA LISTE DU TOURNAMENT CONTROLLER \n")
        # c.print(self.player_list)
        # print("VUE DU TOURNOIS ALIMENTE\n")
        # c.print(self.tournament_list)

    def creat_first_round(self):
        displaay_available_tournement_to_launch = self.tournament_view.display_choose_tournament_to_launch(
            self.tournament_list)
