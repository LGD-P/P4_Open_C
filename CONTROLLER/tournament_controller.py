from rich.console import Console
from datetime import datetime
from operator import itemgetter
from tinydb import TinyDB, Query

from CONTROLLER.player_controller import db

from VIEW.tournament_view import TournamentView
from VIEW.player_view import PlayerView
from VIEW.round_view import RoundView
from VIEW.match_view import MatchView

from MODEL.tournament_model import Tournament
from MODEL.round_model import Round


tournament_tables = db.table("TOURNAMENT")
tournament_tables.truncate()
query = Query()

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
        self.serialized_list_of_players = []
        self.serialized_list_of_score = []
        self.serialized_list_of_tours = []

    def add_tournament(self):
        """This function get dict from tournament_view
        display_add_tournament_form() and instance a tournament in
        tournament_list; add data in database
        """

        serialized_tournament = self.tournament_view.display_add_tournament_form()

        self.tournament_list.append(Tournament(serialized_tournament["name"],
                                               serialized_tournament["place"],
                                               serialized_tournament["date"],
                                               serialized_tournament["tours"],
                                               serialized_tournament["players"],
                                               serialized_tournament["time_control"],
                                               serialized_tournament["description"],
                                               serialized_tournament["player_score"]))

        tournament_tables.insert(serialized_tournament)

    def add_player_in_tournament(self):
        """If a tournament is instanced in touranment_list
        This function get dict from tournament_view,
        display_add_player_in_tournament_form(), and fill tournament 
        with selected player
        The player score is also set on 0 by default
        Add data in database

        Returns:
            None_: return None if there is no tournament in list
        """

        player_in_tournament = self.tournament_view.display_add_player_in_tournament_form(
            self.tournament_list, self.player_list, self.player_view)

        if player_in_tournament == None:
            return None
        else:
            tournament = player_in_tournament["chosen_tournament"]
            player = player_in_tournament["chosen_player"]

            tournament.players.append(player)
            # set player_score to 0 as soon as the player has been added in tournament
            tournament.player_score[player] = 0

            # player_in_tournament["chosen_tournament"].player_score[player_in_tournament] = 0

            # c.print(self.tournament_list)
            #tournament_to_update = tournament.name

            serialized_player = player.serialized_player()

            self.serialized_list_of_players.append(serialized_player)

            self.serialized_list_of_score = tournament.serialize_player_score(
                player)

            c.print(self.serialized_list_of_score)

            tournament_tables.update(
                {"players":  self.serialized_list_of_players}, query.name == tournament.name)

            tournament_tables.update(
                {"player_score":  self.serialized_list_of_score}, query.name == tournament.name)

    def swiss_logic_sorting_round_one(self, tournament_to_run):
        """This function is the first part of swiss logic.
        list of players in tournament to run is sorted by rank and returned

        Args:
            tournament_to_run (instance): tournament choosen by user

        Returns:
            list: players sorted list
        """
        c.print("[bold green]Déjà un round[bold green]\n")
        c.print(
            "[bold red] ***************************\n********************\n[bold red]")

        player_in_tournament_to_run = [
            element[0] for element in sorted(tournament_to_run.player_score.items(),
                                             key=lambda k: (-k[1], k[0].rank))
        ]
        return player_in_tournament_to_run

    def swiss_logic_sorting_round_two_and_more(self, tournament_to_run):
        """This function is the second part of swiss logic,
        called if a first round already exist. Player are then be sorted by score and 
        rank. This function try to avoid matchs who have already been played

        Args:
            tournament_to_run (instance): tournament choosen by user

        Returns:
            list: players list sorted
        """
        winner_to_sort = []
        for round in self.round_list[-1].match_list:
            winner_to_sort += round
            c.print(
                "[bold red] ***************************\n********************\n[bold red]")
            c.print(tournament_to_run.player_score)
            c.print(
                "[bold red] ***************************\n********************\n[bold red]")
            player_in_tournament_to_run = [
                element[0] for element in
                sorted(tournament_to_run.player_score.items(),
                       key=lambda k: (-k[1], k[0].rank))]

            c.print(
                "[bold red] ***************************\n********************\n[bold red]")
            c.print(player_in_tournament_to_run)
            c.print(
                "[bold red] ***************************\n********************\n[bold red]")

            first_list_of_match = []
            for _ in player_in_tournament_to_run:
                first_list_of_match.append(
                    [player_in_tournament_to_run[0], player_in_tournament_to_run[1]])
                player_in_tournament_to_run.remove(
                    player_in_tournament_to_run[0])
                player_in_tournament_to_run.remove(
                    player_in_tournament_to_run[0])

            first_list_of_match.append(
                [player_in_tournament_to_run[-2], player_in_tournament_to_run[-1]])

            for match_1 in first_list_of_match:
                for match_list in tournament_to_run.tours:
                    for match in match_list:
                        if first_list_of_match[-1] == tournament_to_run.tours[-1][-1]:
                            position = first_list_of_match.index(
                                match_1)
                            player_to_move = first_list_of_match[-1][0]
                            player_to_replace = first_list_of_match[-2][0]
                            first_list_of_match[-2].append(
                                player_to_move)
                            first_list_of_match[-1].append(
                                player_to_replace)
                            del (first_list_of_match[-2][0])
                            del (first_list_of_match[-1][0])

                        else:
                            while match == match_1:
                                position = first_list_of_match.index(
                                    match_1)
                                player_to_move = first_list_of_match[position][0]
                                player_to_replace = first_list_of_match[position+1][0]
                                first_list_of_match[position +
                                                    1].append(player_to_move)
                                first_list_of_match[position].append(
                                    player_to_replace)
                                del (
                                    first_list_of_match[position+1][0])
                                del (first_list_of_match[position][0])
        return first_list_of_match

    def swiss_logic_result(self, player_in_tournament_to_run, tournament_to_run):
        """This function is the last part of swiss logic. Sorted players list is 
        cut in half and ina  loop matchs are created.

        Args:
            player_in_tournament_to_run (list): player sorted
            tournament_to_run (instance): tournament choosen by yser

        Returns:
            instance: tournament choosen with tours attribute filled.
        """
        half_list = len(player_in_tournament_to_run)//2

        first_part = player_in_tournament_to_run[0:half_list]

        second_part = player_in_tournament_to_run[half_list:9]

        ###################################################

        first_list_of_match = []
        for element_1, element_2 in zip(first_part, second_part):
            first_list_of_match.append([element_1, element_2])

            self.serialized_list_of_tours.append([
                f" {element_1.last_name} {element_1.first_name} == CONTRE ==>"
                f" {element_2.last_name} {element_2.first_name}"])

        # add  round list in tournament chosen
        tournament_to_run.tours.append(
            first_list_of_match)
        # c.print(tournament_to_run.player_score)

        for tournament in self.started_tournaments:
            if tournament_to_run.name in tournament.name:
                tournament.tours = tournament_to_run.tours

        return tournament_to_run

    def creat_round(self):
        """This function used swiss logic to creat a tour

        Returns:
            instance: tournament instance filled with new tour
        """
        tournament_to_run = self.tournament_view.display_choose_a_tournament_to_launch(
            self.tournament_list)

        if tournament_to_run == None:
            return None
        else:
            self.started_tournaments.append(tournament_to_run)

            #################################
            # DEBUG ZONE FOR SORTING
            #################################

            if not self.round_list:
                c.print("[bold red]pas encore de round [bold red]\n")

                player_in_tournament_to_run = sorted(
                    tournament_to_run.player_score.keys(), key=lambda k: (k.rank)
                )

            elif len(self.round_list) == 1:
                player_in_tournament_to_run = self.swiss_logic_sorting_round_one(
                    tournament_to_run)

                # c.print(tournament_to_run.player_score)

                # continue swiss logic by rank

            elif len(self.round_list) > 1:
                first_list_of_match = self.swiss_logic_sorting_round_two_and_more(
                    tournament_to_run)

                # add first round list in tournament chosen
                tournament_to_run.tours.append(
                    first_list_of_match)

                for tournament in self.started_tournaments:
                    if tournament_to_run.name in tournament.name:
                        tournament.tours = tournament_to_run.tours

                c.print(
                    "[bold red] ***************************\n********************\n[bold red]")
                c.print(tournament_to_run.tours[-1])
                c.print(
                    "[bold red] ***************************\n********************\n[bold red]")

                return tournament_to_run

        tournament_with_new_round = self.swiss_logic_result(
            player_in_tournament_to_run, tournament_to_run)

        return tournament_with_new_round

    def fill_round_instance_creat_announcement(self):
        """This function use create_round() to creat instance of round 
        """

        tournament_running = self.creat_round()
        if tournament_running == None:
            return None
        else:
            self.round_view.display_round_view(
                tournament_running)

            # fill round instance with match
            # Check if there is a round else creat round

            if not self.round_list:
                starting_hour = datetime.now()
                self.round_list.append(
                    Round(tournament_running.tours[-1], f"Round {1}",
                          starting_hour,
                          None, 1, tournament_running.name)
                )

                # self.serialized_list_of_tours = tournament_running.serialize_tours()

                tournament_tables.update(
                    {"tours":  self.serialized_list_of_tours}, query.name == tournament_running.name)
            else:
                # if there is a round(s) in list
                # check if there is ending hour else add new round  as 2nd  3rd etc..
                match_concerned = len(tournament_running.tours)
                starting_hour = datetime.now()
                self.round_list.append(
                    Round(tournament_running.tours[match_concerned - 1], f"Round {len(self.round_list) + 1}",
                          starting_hour,
                          None, 1, tournament_running.name))

                # self.serialized_list_of_tours = tournament_running.serialize_tours()

                tournament_tables.update(
                    {"tours":  self.serialized_list_of_tours}, query.name == tournament_running.name)

            # print de débug
            """c.print("[green]****************************[green]")
            c.print("[red]******************************[red]")
            c.print(self.round_view.debug_print(self.round_list))
            c.print("[green]****************************[green]")
            c.print("[red]******************************[red]")"""

    def add_player_point(self, winner_choice, tournament_choice, match_list):
        """This function will be user to add tournament.player_score result. 

        Args:
            winner_choice (int): will be input from 
                match_view.display_tournament_to_fill_result()
            tournament_choice (instance): tournament
            match_list (instance attribute): tounrnament.tours
        """

        if int(winner_choice) == 2:
            for player in tournament_choice.player_score:
                if player == match_list[0]:
                    tournament_choice.player_score[player] += 0.5
                    self.serialized_list_of_score[f"{player.last_name}, {player.first_name}"] = 0.5

                elif player == match_list[1]:
                    tournament_choice.player_score[player] += 0.5
                    self.serialized_list_of_score[f"{player.last_name}, {player.first_name}"] += 0.5

        elif int(winner_choice) == 0:
            for player in tournament_choice.player_score:
                if player == match_list[0]:
                    tournament_choice.player_score[player] += 1
                    self.serialized_list_of_score[f"{player.last_name}, {player.first_name}"] = 1
                elif player == match_list[1]:
                    tournament_choice.player_score[player] += 0
                    self.serialized_list_of_score[f"{player.last_name}, {player.first_name}"] = 0

        elif int(winner_choice) == 1:
            for player in tournament_choice.player_score:
                if player == match_list[0]:
                    tournament_choice.player_score[player] += 0
                    self.serialized_list_of_score[f"{player.last_name}, {player.first_name}"] += 0
                elif player == match_list[1]:
                    tournament_choice.player_score[player] += 1
                    self.serialized_list_of_score[f"{player.last_name}, {player.first_name}"] += 1

        tournament_tables.update(
            {"player_score":  self.serialized_list_of_score}, query.name == tournament_choice.name)

    def fill_result(self):
        """This function using add_player_point() fill tournament instance.player_score 
        and 
        round instance.
        """
        tournament_choice = self.match_view.display_tournament_to_fill_result(
            self.started_tournaments, self.tournament_list)

        round_index = (len(tournament_choice.tours))

        round = tournament_choice.tours[round_index - 1]

        for match_list in round:
            winner_choice = self.match_view.display_player_in_tournament_to_fill_score(
                tournament_choice, match_list)

            self.add_player_point(winner_choice, tournament_choice, match_list)

            # c.print(tournament_choice)

        for tournament in self.started_tournaments:
            for round in self.round_list:
                if tournament.name == round.tournament_name:
                    if round.ending_hour == None:
                        round.ending_hour = datetime.now()

    def report(self):
        """This function using tournament.view.display_report()
        allow acces to report menu. 
        """
        self.tournament_view.display_report(
            self.tournament_list, self.round_list)
