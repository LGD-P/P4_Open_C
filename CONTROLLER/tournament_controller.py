from datetime import datetime

from rich.console import Console

from CONTROLLER.match_controller import MatchController
from MODEL.player_model import Player
from MODEL.round_model import Round
from MODEL.tournament_model import Tournament
from VIEW.error_and_user_messages import ErrorAndUserMessages
from VIEW.match_view import MatchView
from VIEW.player_view import PlayerView
from VIEW.round_view import RoundView
from VIEW.tournament_view import TournamentView

c = Console()


class TournamentController:
    def __init__(self, tournament_list, player_list):
        self.tournament_view = TournamentView()
        self.tournament_list = tournament_list
        self.player_view = PlayerView()
        self.player_list = player_list
        self.round_view = RoundView()
        self.match_view = MatchView()
        self.match_controller = MatchController()

    def add_tournament(self):
        """This function get dict from tournament_view
        display_add_tournament_form() and instance a tournament in
        tournament_list; add data in database
        """

        serialized_tournament = self.tournament_view \
            .display_add_tournament_form()

        self.tournament_list.append(Tournament(
            serialized_tournament["name"],
            serialized_tournament["date"],
            serialized_tournament["place"],
            serialized_tournament["tours"],
            serialized_tournament["players"],
            serialized_tournament["time_control"],
            serialized_tournament["description"],
            serialized_tournament["player_score"]))

    def add_player_in_tournament(self):
        """If a tournament is instanced in tournament_list
        This function get dict from tournament_view,
        display_add_player_in_tournament_form(), and fill tournament
        with selected player
        The player score is also set on 0 by default
        Add data in database

        Returns:
            None_: return None if there is no tournament in list
        """

        player_in_tournament = self.tournament_view \
            .display_add_player_in_tournament_form(
                self.tournament_list, self.player_list, self.player_view)

        if not player_in_tournament:
            return None
        else:
            tournament = player_in_tournament["chosen_tournament"]
            player = player_in_tournament["chosen_player"]

            tournament.players.append(player)
            # set player_score to 0 as soon as the player has
            # been added in tournament
            tournament.player_score[player] = 0

            for player in tournament.players:
                tournament.memory_of_enconters[player] = []

    def matchmaking_round_one(self, tournament_to_run):
        """This function is the last part of swiss logic. Sorted players list
        is cut in half and ina loop matches are created.

        Args:
            tournament_to_run (instance): tournament chose by user

        Returns:
            instance: tournament chose with tours attribute filled.
        """

        player_in_tournament_to_run = sorted(
            tournament_to_run.player_score.keys(),
            key=lambda k: k.rank
        )

        half_list = len(player_in_tournament_to_run) // 2

        first_part = player_in_tournament_to_run[:half_list]
        # print(first_part)

        second_part = player_in_tournament_to_run[half_list:]
        # print(second_part)
        ###################################################

        list_of_match = []

        for element_1, element_2 in zip(first_part, second_part):
            list_of_match.append([element_1, element_2])

        # add  round list in tournament chosen
        match_list = self.match_controller.add_unique_match_list(
            list_of_match, tournament_to_run.player_score)

        starting_hour = datetime.now()

        tour = Round(match_list, f"Round {len(tournament_to_run.tours) + 1}",
                     starting_hour, None, len(tournament_to_run.tours) + 1, tournament_to_run.name)

        tournament_to_run.tours.append(tour)

    def matchmaking_next_round(self, tournament_to_run):
        player_in_tournament_to_run = [
            element[0] for element in
            sorted(tournament_to_run.player_score.items(),
                   key=lambda k: (-k[1], k[0].rank))]

        list_of_match = []

        associated_players = []
        for player in player_in_tournament_to_run:
            if player in associated_players:
                continue

            list_of_opponent = [
                p for p in player_in_tournament_to_run if p != player and p not in associated_players]
            for opponent in list_of_opponent:
                if self.has_players_already_played_together(tournament_to_run, player, opponent):
                    continue
                list_of_match.append([player, opponent])
                associated_players.append(player)
                associated_players.append(opponent)
                break

            if player not in associated_players:
                list_of_match.append([player, list_of_opponent[0]])
                associated_players.append(player)
                associated_players.append(list_of_opponent[0])

        # add  round list in tournament chosen
        match_list = self.match_controller.add_unique_match_list(
            list_of_match, tournament_to_run.player_score)

        starting_hour = datetime.now()

        tour = Round(match_list, f"Round {len(tournament_to_run.tours) + 1}",
                     starting_hour, None, len(tournament_to_run.tours) + 1, tournament_to_run.name)

        tournament_to_run.tours.append(tour)

    def has_players_already_played_together(self, tournament, player, opponent):
        for tour in tournament.tours:
            for match in tour.match_list:
                if match[0][0] == player and match[1][0] == opponent:
                    return True
                if match[1][0] == player and match[0][0] == opponent:
                    return True
        return False

    def create_round(self):
        """This function used swiss logic to create a tour

        Returns:
            instance: tournament instance filled with new tour
        """

        tournament_to_run = self.tournament_view.display_choose_a_tournament_to_launch(
            self.tournament_list)

        if not tournament_to_run:
            return None
        else:
            if len(tournament_to_run.tours) == 4:
                """
                c.print(
                    "[bold red] ******************\n************\n[bold red]")
                c.print(tournament_to_run.player_score)
                c.print(
                    "[bold red] ******************\n************\n[bold red]")
                """
                player_in_tournament_to_run = [
                    element[0] for element in
                    sorted(tournament_to_run.player_score.items(),
                           key=lambda k: (-k[1], k[0].rank))]

                winner = player_in_tournament_to_run[0]

                return self.tournament_view.display_winner(
                    winner, tournament_to_run.player_score[winner])

            #################################
            # DEBUG ZONE FOR SORTING
            #################################

            if len(tournament_to_run.tours) == 0:
                self.matchmaking_round_one(tournament_to_run)
            else:
                self.matchmaking_next_round(tournament_to_run)
            return tournament_to_run

    def fill_round_instance_create_announcement(self):
        """This function use create_round() to create instance of round
        """

        tournament_running = self.create_round()
        self.round_view.display_launching_round_view(tournament_running)

    def add_player_point(self, winner_choice, tournament_choice, match_list):
        """This function will be user to add tournament.player_score result.

        Args:
            winner_choice (int): will be input from
                match_view.display_tournament_to_fill_result()
            tournament_choice (instance): tournament
            match_list (instance attribute): tournament.tours
        """

        if int(winner_choice) == 2:
            for player in tournament_choice.player_score:
                if player == match_list[0][0]:
                    tournament_choice.player_score[player] += 0.5
                    match_list[0][1] += 0.5
                    tournament_choice.memory_of_enconters[player].append(
                        match_list[1][0])

                elif player == match_list[1][0]:
                    tournament_choice.player_score[player] += 0.5
                    match_list[1][1] += 0.5
                    tournament_choice.memory_of_enconters[player].append(
                        match_list[0][0])

        elif int(winner_choice) == 0:
            for player in tournament_choice.player_score:
                if player == match_list[0][0]:
                    tournament_choice.player_score[player] += 1
                    match_list[0][1] += 1
                    tournament_choice.memory_of_enconters[player].append(
                        match_list[1][0])

                elif player == match_list[1][0]:
                    tournament_choice.player_score[player] += 0
                    match_list[1][1] += 0
                    tournament_choice.memory_of_enconters[player].append(
                        match_list[0][0])

        elif int(winner_choice) == 1:
            for player in tournament_choice.player_score:
                if player == match_list[0][0]:
                    tournament_choice.player_score[player] += 0
                    match_list[0][1] += 0
                    tournament_choice.memory_of_enconters[player].append(
                        match_list[1][0])

                elif player == match_list[1][0]:
                    tournament_choice.player_score[player] += 1
                    match_list[1][1] = 1
                    tournament_choice.memory_of_enconters[player].append(
                        match_list[0][0])

    def fill_result(self):
        """This function using add_player_point() fill tournament
        instance.player_score and round instance.
        """
        tournament_choice = self.match_view.display_tournament_to_fill_result(
            self.tournament_list)

        if not tournament_choice:
            return None

        tour = tournament_choice.tours[-1]
        for match_list in tour.match_list:
            winner_choice = self.match_view \
                .display_player_in_tournament_to_fill_score(
                    tournament_choice, match_list)

            self.add_player_point(winner_choice, tournament_choice,
                                  match_list)

            # c.print(tournament_choice)

        tour.ending_hour = datetime.now()

    def generate_data(self):
        """Use this feature to quickly set up a tournament with a list of
        players so you can test the functionality of the program"""
        self.player_list.clear()
        self.tournament_list.clear()

        quick_players_list = [
            Player("DENIS", "Laurent", "11-12-2000", "h", 1),
            Player("CHARLES", "Henri", "11-10-2005", "h", 2),
            Player("MOINE", "Alice", "10-10-1990", "f", 3),
            Player("VAULT", "Lise", "01-02-1980", "f", 4),
            Player("CREPIN", "Maurice", "12-07-1950", "h", 5),
            Player("TIAGO", "Daniela", "05-06-1977", "f", 6),
            Player("EDON", "Anna", "09-03-1985", "f", 7),
            Player("PRIMO", "Angelo", "09-03-1970", "h", 8)]

        for players in quick_players_list:
            self.player_list.append(players)

        quick_tournament = [
            Tournament("PARIS Chess-Event", "Paris",
                       datetime.now().strftime("%d-%m-%Y"),
                       [], quick_players_list[0:9], "Blitz",
                       "Description", {}, 4)
        ]

        for tournament in quick_tournament:
            for player in tournament.players:
                tournament.player_score[player] = 0
                tournament.memory_of_enconters[player] = []

        for tournament in quick_tournament:
            self.tournament_list.append(tournament)

        ErrorAndUserMessages().operation_done()
