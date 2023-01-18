from rich.console import Console
from datetime import datetime


from VIEW.tournament_view import TournamentView
from VIEW.player_view import PlayerView
from VIEW.round_view import RoundView
from VIEW.match_view import MatchView

from MODEL.tournament_model import Tournament
from MODEL.round_model import Round
from MODEL.match_model import Match


c = Console()


class TournamentController:
    def __init__(self, tournament_list, player_list, round_list, match_list):
        self.tournament_view = TournamentView()
        self.tournament_list = tournament_list
        self.player_view = PlayerView()
        self.player_list = player_list
        self.round_view = RoundView()
        self.round_list = round_list
        self.match_view = MatchView()
        self.match_list = match_list

    def add_tournament(self):

        tournament = self.tournament_view.display_add_tournament_form()

        self.tournament_list.append(Tournament(tournament["name"], tournament["place"],
                                    tournament["date"], tournament["tours"],
                                    tournament["players"], tournament["time_control"],
                                    tournament["description"]))
        # print de débug
        # c.print(self.tournament_list)

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
        display_available_tournement_to_launch = self.tournament_view.display_choose_tournament_to_launch(
            self.tournament_list)

        if not display_available_tournement_to_launch:
            pass
        else:

            tournament_to_run = self.tournament_list[int(
                display_available_tournement_to_launch)]

            tournament_to_run = sorted(tournament_to_run.players,
                                       key=lambda player: player.rank)

            first_part = tournament_to_run[0:4]
            second_part = tournament_to_run[4:9]

            first_list_of_match = []
            for element_1, element_2 in zip(first_part, second_part):
                first_list_of_match.append([element_1, element_2])

            # add first round list in tournament chosen
            self.tournament_list[
                int(display_available_tournement_to_launch)
            ].tours.append(first_list_of_match)

        # c.print(self.tournament_list[
            #    int(display_available_tournement_to_launch)
            # ])

            # c.print(first_list_of_match)
            return first_list_of_match

    def fill_round_instance(self):
        first_list_of_round = self.creat_first_round()

        self.round_view.display_round_view(first_list_of_round)

        for tournament in self.tournament_list:
            if first_list_of_round in tournament.tours:

                self.round_list.append(
                    Round(first_list_of_round, "Round_1",
                          datetime.now().strftime("%d-%m-%Y"),
                          f"Début de round : {datetime.now().strftime('%H:%M:%S')}",
                          f"Heure de fin : à venir",
                          1, tournament.name)
                )

        c.print(self.round_list)

    def add_result(self):
        self.match_view.display_match_to_add_result(self.tournament_list)
