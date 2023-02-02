from rich.console import Console
from datetime import datetime
from operator import itemgetter


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
        self.started_tournaments = []

    def add_tournament(self):

        tournament = self.tournament_view.display_add_tournament_form()

        self.tournament_list.append(Tournament(tournament["name"], tournament["place"],
                                    tournament["date"], tournament["tours"],
                                    tournament["players"], tournament["time_control"],
                                    tournament["description"], tournament["player_score"]))
        # print de débug
        # c.print(self.tournament_list)

    def add_player_in_tournament(self):

        player_in_tournament = self.tournament_view.display_add_player_in_tournament_form(
            self.tournament_list, self.player_list)

        if player_in_tournament == None:
            return None
        else:
            # set player_score to 0 as soon as the player has been added in tournament
            player_in_tournament["chosen_tournament"].player_score[player_in_tournament] = 0

            c.print(self.tournament_list)

    def creat_first_round(self):

        display_available_tournement_to_launch = self.tournament_view.display_choose_tournament_to_launch(
            self.tournament_list)

        if display_available_tournement_to_launch == None:
            return None
        else:
            # get tournament choice to run
            tournament_to_run = display_available_tournement_to_launch

            # add tounrament in started list tournament
            self.started_tournaments.append(tournament_to_run)

            #################################
            # DEBUG ZONE FOR SORTING
            #################################

            if self.round_list == []:
                c.print("[bold red]pas encore de round [bold red]\n")

                player_in_tournament_to_run = sorted(
                    tournament_to_run.player_score.keys(), key=lambda k: (k.rank)
                )

                """
                elif len(self.round_list[-1].match_list) == 1:
                    the_winner_is = (self.round_list[-1].match_list[0])

                    sorted_element = sorted(
                        the_winner_is, key=lambda k: (-k['score'], k["player_rank"]))

                    #  c.print(sorted_element)

                    half_part = len(sorted_element)//2

                    winner = sorted_element[0:half_part]

                    c.print(
                        f"[bold red] On dirait que ce tournois compte un vainqueur[bold red]"
                        f" félicitation à :"
                        f" {winner[0]['player'].last_name} "
                        f" {winner[0]['player'].first_name}")
                    return None
                """

            else:

                c.print("[bold green]Déjà un round[bold green]\n")
                c.print(
                    "[bold red] ***************************\n********************\n[bold red]")

                winner_to_sort = []
                for round in self.round_list[-1].match_list:
                    winner_to_sort += round

                # c.print(winner_to_sort)

                c.print(
                    "[bold blue] ***************************\n********************\n[bold blue]")
                """
                sorted_element = sorted(
                    winner_to_sort, key=lambda k: (-k['score'], k["player_rank"]))
                """
                player_in_tournament_to_run = [
                    element[0] for element in
                    sorted(tournament_to_run.player_score.items(),
                           key=lambda k: (-k[1], k[0].rank))
                ]

                #  c.print(sorted_element)
                """
                half_part = len(sorted_element)//2

                winner = sorted_element[0:half_part]
                c.print(
                    f"[bold blue] LES GAGNANTS SONT :\n {winner}[bold blue]")

               # c.print(winner)
                # c.print(
                #   "[bold red] ***************************\n********************\n[bold red]")

                tournament_to_run_players = sorted(
                    winner, key=lambda k: (-k["score"], k["player_rank"]))

                """
                # c.print(
             # "[bold red] ***************************\n********************\n[bold red]")
            # c.print(tournament_to_run_players)

            # continue swiss logic by rank

            half_list = len(player_in_tournament_to_run)//2

            first_part = player_in_tournament_to_run[0:half_list]

            # print de début
            """c.print("[green]****************************[green]")
            c.print("[red]******************************[red]")
            c.print("[red]PREMIERE PARTIE DU GROUPE[red]")
            c.print(first_part)
            c.print("[green]****************************[green]")
            c.print("[red]******************************[red]\n\n")
            print("\n")
            """
            second_part = player_in_tournament_to_run[half_list:9]

            # print de début
            """
            c.print("[green]****************************[green]")
            c.print("[red]******************************[red]")
            c.print("[red]DEIXIEME PARTIE DU GROUPE[red]")
            c.print(second_part)
            c.print("[green]****************************[green]")
            c.print("[red]******************************[red]")
            """
            ###################################################
            ###################################################

            first_list_of_match = []
            for element_1, element_2 in zip(first_part, second_part):
                first_list_of_match.append([element_1, element_2])

            # add first round list in tournament chosen
            tournament_to_run.tours.append(
                first_list_of_match)
            # c.print(tournament_to_run)

            for tournament in self.started_tournaments:
                if tournament_to_run.name in tournament.name:
                    tournament.tours = tournament_to_run.tours

            return tournament_to_run

    def fill_round_instance_creat_announcement(self):
        tournament_running = self.creat_first_round()
        if tournament_running == None:
            return None
        else:

            self.round_view.display_round_view(
                tournament_running)

            # fill round instance with match
            # Check if there is a round else creat round

            if len(self.round_list) == False:
                starting_hour = datetime.now()
                self.round_list.append(
                    Round(tournament_running.tours[-1], f"Round {1}",
                          starting_hour,
                          None, 1, tournament_running.name)
                )
            else:
                # if there is a round(s) in list
                # check if there is ending hour else add new round  as 2nd  3rd etc..
                match_concerned = len(tournament_running.tours)
                for round in self.round_list:
                    if round.ending_hour:
                        starting_hour = datetime.now()
                        self.round_list.append(
                            Round(tournament_running.tours[match_concerned - 1], f"Round {len(self.round_list) + 1}",
                                  starting_hour,
                                  None, 1, tournament_running.name))

            # print de débug
            """c.print("[green]****************************[green]")
            c.print("[red]******************************[red]")
            c.print(self.round_view.debug_print(self.round_list))
            c.print("[green]****************************[green]")
            c.print("[red]******************************[red]")"""

    def add_result(self):
        c.print(self.tournament_list)
        # gérer la logique de résultat avec le dictionnaire
        # dans la match view  créer les élements qui vont être récupérer ici.
        tournament_choice = self.match_view.display_tournament_to_fill_result(
            self.started_tournaments, self.tournament_list)

        round_index = (len(tournament_choice.tours))

        round = tournament_choice.tours[round_index - 1]
        index = -1

        for match_list in round:
            winner_choice = self.match_view.display_player_in_tournament_to_fill_score(
                tournament_choice, match_list)

            if int(winner_choice) == 2:
                for player in tournament_choice.player_score:
                    if player == match_list[0]:

                        tournament_choice.player_score[player] += 0.5
                    elif player == match_list[1]:
                        tournament_choice.player_score[player] += 0.5

            elif int(winner_choice) == 0:
                for player in tournament_choice.player_score:
                    if player == match_list[0]:
                        tournament_choice.player_score[player] += 1
                    elif player == match_list[1]:
                        tournament_choice.player_score[player] += 0

            elif int(winner_choice) == 1:
                for player in tournament_choice.player_score:
                    if player == match_list[0]:
                        tournament_choice.player_score[player] += 0
                    elif player == match_list[1]:
                        tournament_choice.player_score[player] += 1

            # c.print(tournament_choice)

        for tournament in self.started_tournaments:
            for round in self.round_list:
                if tournament.name == round.tournament_name:
                    if round.ending_hour == None:
                        round.ending_hour = datetime.now()

        c.print(self.round_list.__repr__())
        """
        # print de débug
        c.print(self.tournament_list)
        c.print("[green]****************************[green]")
        c.print("[red]******************************[red]")
        c.print(self.round_list)
        c.print("[green]****************************[green]")
        c.print("[red]******************************[red]")"""
