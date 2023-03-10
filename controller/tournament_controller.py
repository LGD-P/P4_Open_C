from datetime import datetime

from rich.console import Console

from controller.match_controller import MatchController
from model.round_model import Round
from model.tournament_model import Tournament
from view.error_and_user_messages import ErrorAndUserMessages
from view.match_view import MatchView
from view.player_view import PlayerView
from view.round_view import RoundView
from view.tournament_view import TournamentView

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
                tournament.memory_of_enconters[str(player)] = []

    def matchmaking_round_one(self, tournament_to_run):
        """This function is the last part of swiss logic. Sorted players list
        is cut in half and ina loop matches are created.

        Args:
            tournament_to_run (instance): tournament chose by user

        Returns:
            instance: tournament chose with tours attribute filled.
        """

        player_in_tournament_to_run = sorted(tournament_to_run.player_score.keys(), key=lambda k: k.rank)

        half_list = len(player_in_tournament_to_run) // 2

        first_part = player_in_tournament_to_run[:half_list]

        second_part = player_in_tournament_to_run[half_list:]

        list_of_match = []

        for element_1, element_2 in zip(first_part, second_part):
            list_of_match.append([element_1, element_2])

        # add  round list in tournament chosen
        match_list = self.match_controller.add_unique_match_list(list_of_match, tournament_to_run.player_score)

        starting_hour = datetime.now()

        tour = Round(match_list, f"Round {len(tournament_to_run.tours) + 1}",
                     starting_hour, None, len(tournament_to_run.tours) + 1, tournament_to_run.name)

        tournament_to_run.tours.append(tour)

    def matchmaking_next_round(self, tournament_to_run):
        """This function sorted player by score -k and rank k and creat a list of oponent
        to each players, if players are not in this list match can be created

        Args:
            tournament_to_run (instance): instance of tournament chosen by user
        """
        player_in_tournament_to_run = [element[0] for element in sorted(tournament_to_run.player_score.items(),
                                                                        key=lambda k: (-k[1], k[0].rank))]
        # Will be filled with match
        list_of_match = []
        # Will be used to creat news round
        associated_players = []
        for player in player_in_tournament_to_run:
            if player in associated_players:
                continue  # first loop is obviously empty we need to continue

            # Start to creat a list of oponants from player_in_tournament and associated_players
            # As in the first loop, associated player is empty, all players are in.
            # then list_of_opponent decrease, because oponent will be added in the next tow loops .
            list_of_opponent = [p for p in player_in_tournament_to_run if p != player and p not in associated_players]

            # here we check if players has already played togather returning True, adding
            # player and opponent in associated_player, else break logic
            for opponent in list_of_opponent:
                if self.has_players_already_played_together(tournament_to_run, player, opponent):
                    continue
                list_of_match.append([player, opponent])
                associated_players.append(player)
                associated_players.append(opponent)

                break
            # Then we can creat a match and add it in list_of_match
            # Finaly we add player and oponent in associated_player for next loop.
            if player not in associated_players:
                list_of_match.append([player, list_of_opponent[0]])
                associated_players.append(player)
                associated_players.append(list_of_opponent[0])

        # Creat match list
        match_list = self.match_controller.add_unique_match_list(list_of_match, tournament_to_run.player_score)

        starting_hour = datetime.now()
        # Creat Round()
        tour = Round(match_list, f"Round {len(tournament_to_run.tours) + 1}",
                     starting_hour, None, len(tournament_to_run.tours) + 1, tournament_to_run.name)

        tournament_to_run.tours.append(tour)

    def has_players_already_played_together(self, tournament, player, opponent):
        """This function check match possibilities regardless that
        Pierre vs Paul is the same match as Paul vs Pierre. Used in a loop
        it allowd to creat match that were not been played
        Args:
            tournament (instance): intance of tournament
            player (instance): player instance
            opponent (instance): player instance as opponent

        Returns:
            Bool: True or False
        """
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

                player_in_tournament_to_run = [
                    element[0] for element in
                    sorted(tournament_to_run.player_score.items(),
                           key=lambda k: (-k[1], k[0].rank))]

                winner = player_in_tournament_to_run[0]

                return self.tournament_view.display_winner(
                    winner, tournament_to_run.player_score[winner])

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

    def winner_choice_zero(self, winner_choice, tournament_choice, match_list):
        if int(winner_choice) == 0:
            for player in tournament_choice.player_score:
                if player == match_list[0][0]:
                    tournament_choice.player_score[player] += 1
                    match_list[0][1] = 1
                    tournament_choice.memory_of_enconters[str(player)].append(
                        match_list[1][0])

                elif player == match_list[1][0]:
                    tournament_choice.player_score[player] += 0
                    match_list[1][1] = 0
                    tournament_choice.memory_of_enconters[str(player)].append(
                        match_list[0][0])

    def winner_choice_one(self, winner_choice, tournament_choice, match_list):
        if int(winner_choice) == 1:
            for player in tournament_choice.player_score:
                if player == match_list[0][0]:
                    tournament_choice.player_score[player] += 0
                    match_list[0][1] = 0
                    tournament_choice.memory_of_enconters[str(player)].append(
                        match_list[1][0])

                elif player == match_list[1][0]:
                    tournament_choice.player_score[player] += 1
                    match_list[1][1] = 1
                    tournament_choice.memory_of_enconters[str(player)].append(
                        match_list[0][0])

    def winner_choice_tow(self, winner_choice, tournament_choice, match_list):
        if int(winner_choice) == 2:
            for player in tournament_choice.player_score:
                if player == match_list[0][0]:
                    tournament_choice.player_score[(player)] += 0.5
                    match_list[0][1] = 0.5
                    tournament_choice.memory_of_enconters[str(player)].append(
                        match_list[1][0])

                elif player == match_list[1][0]:
                    tournament_choice.player_score[player] += 0.5
                    match_list[1][1] = 0.5
                    tournament_choice.memory_of_enconters[str(player)].append(
                        match_list[0][0])

    def add_player_point(self, winner_choice, tournament_choice, match_list):
        """This function will be user to add tournament.player_score result.

        Args:
            winner_choice (int): will be input from
                match_view.display_tournament_to_fill_result()
            tournament_choice (instance): tournament
            match_list (instance attribute): tournament.tours
        """
        if not tournament_choice.memory_of_enconters:
            for players in tournament_choice.players:
                tournament_choice.memory_of_enconters[str(players)] = []

        if not tournament_choice.memory_of_enconters and len(tournament_choice.tours) > 0:

            for players in tournament_choice.players:
                tournament_choice.memory_of_enconters[str(players)] = []

        self.winner_choice_zero(winner_choice, tournament_choice, match_list)
        self.winner_choice_one(winner_choice, tournament_choice, match_list)
        self.winner_choice_tow(winner_choice, tournament_choice, match_list)

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

        tour.ending_hour = datetime.now()
        ErrorAndUserMessages().score_added()
