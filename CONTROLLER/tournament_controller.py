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
            # get tournament choice to run
            tournament_to_run = display_available_tournement_to_launch

            # sort players of this tournament
            # mylist = sorted(mylist, key=lambda k: (k['name'].lower(), k['age'])) ! tuple
            tournament_to_run_players = sorted(tournament_to_run.players,
                                               key=lambda player: player.rank)

            # continue swiss logic by rank
            # utiliser len(list//2)
            first_part = tournament_to_run_players[0:4]
            second_part = tournament_to_run_players[4:9]

            first_list_of_match = []
            for element_1, element_2 in zip(first_part, second_part):
                first_list_of_match.append([element_1, element_2])

            # add first round list in tournament chosen
            tournament_to_run.tours.append(
                first_list_of_match)
            c.print(tournament_to_run)

            return tournament_to_run

    def fill_round_instance_creat_announcement(self):
        tournament_running = self.creat_first_round()

        self.round_view.display_round_view(
            tournament_running)

        # fill round instance with match
        self.round_list.append(
            Round(tournament_running.tours, "Round_1",
                  datetime.now().strftime("%d-%m-%Y"),
                  f"Début de round : {datetime.now().strftime('%H:%M:%S')}",
                  f"Heure de fin : à venir",
                  1, tournament_running.name)
        )

        # c.print(self.round_list)

    def add_result(self):
        index = -1
        for tournament in self.tournament_list:
            for match_list in tournament.tours:
                for player in match_list:
                    index += 1
                    # use match_view to get the input result back
                    player_score = self.match_view.display_match_to_add_result(
                        self.tournament_list)

                    # set ending hours of round
                    self.round_list[0].ending_hour = f"Heure de fin : "\
                        f"{datetime.now().strftime('%H:%M:%S')}"

                    # give each players points
                    if int(player_score) == 0:
                        tournament.player_score[
                            f"{player[0].last_name} {player[0].first_name}"
                        ] = 1
                        tournament.player_score[
                            f"{player[1].last_name} {player[1].first_name}"
                        ] = 0

                    elif int(player_score) == 1:
                        tournament.player_score[
                            f"{player[0].last_name} {player[0].first_name}"
                        ] = 0
                        tournament.player_score[
                            f"{player[1].last_name} {player[1].first_name}"
                        ] = 1

                    elif int(player_score) == 2:
                        tournament.player_score[
                            f"{player[0].last_name} {player[0].first_name}"
                        ] = 0.5
                        tournament.player_score[
                            f"{player[1].last_name} {player[1].first_name}"
                        ] = 0.5

                c.print(tournament)

        #c.print("\n\n[bold red]*************************[bold red]")
        #c.print("[bold red]*************************[bold red]")
        # c.print(self.tournament_list[1])
        #c.print("[bold red]*************************[bold red]")
        #c.print("[bold red]*************************[bold red]")
        # c.print(self.round_list)
        #c.print("[bold red]*************************[bold red]")
        #c.print("[bold red]*************************[bold red]")

    def load_winner_for_round_2(self):
        winner_list = []

        # Using the round 1 list updated with players score
        # we build a winner list for the next round

        for players in self.round_list[0].match_list:

            if players[0].points > players[1].points:
                winner_list.append(players[0])

            elif players[1].points > players[0].points:
                winner_list.append(players[1])

            else:
                if players[0].rank < players[1].rank:

                    winner_list.append(players[0])
                else:
                    winner_list.append(players[1])

        c.print(sorted(winner_list, key=lambda players:
                       (players.points), reverse=True))

        return sorted(winner_list, key=lambda players:
                      (players.points), reverse=True)

    def creat_second_round(self):

        # Using the winner list we sort and creat next round

        display_second_round = self.load_winner_for_round_2()

        first_part_round2 = display_second_round[0:2]
        second_part_round2 = display_second_round[2:4]

        second_list_of_match = []
        for element_1, element_2 in zip(first_part_round2, second_part_round2):
            second_list_of_match.append([element_1, element_2])

        # add first round list in tournament chosen
        self.tournament_list[1].tours.append(second_list_of_match)

        c.print(self.tournament_list[1])

        self.round_view.display_round_view(second_list_of_match)

        return second_list_of_match
