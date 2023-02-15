from rich.console import Console
from datetime import datetime
from tinydb import TinyDB
import json

from CONTROLLER.match_controller import MatchController
from CONTROLLER.db_controller import DataBase


from VIEW.tournament_view import TournamentView
from VIEW.player_view import PlayerView
from VIEW.round_view import RoundView
from VIEW.match_view import MatchView

from MODEL.tournament_model import Tournament
from MODEL.round_model import Round
from MODEL.player_model import Player
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
        self.match_controller = MatchController()
        self.unique_match_list = []
        self.started_tournaments = []
        self.db = DataBase()
        self.serialized_list_of_players = {}
        self.serialized_list_of_score = {}
        self.serialized_list_of_tours = []

    def add_tournament(self):
        """This function get dict from tournament_view
        display_add_tournament_form() and instance a tournament in
        tournament_list; add data in database
        """

        serialized_tournament = self.tournament_view \
            .display_add_tournament_form()

        self.tournament_list.append(Tournament(
            serialized_tournament["name"],
            serialized_tournament["place"],
            serialized_tournament["date"],
            serialized_tournament["tours"],
            serialized_tournament["players"],
            serialized_tournament["time_control"],
            serialized_tournament["description"],
            serialized_tournament["player_score"]))

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

            # player_in_tournament["chosen_tournament"] \
            # .player_score[player_in_tournament] = 0

            # c.print(self.tournament_list)
            # tournament_to_update = tournament.name

    def swiss_logic_sorting_round_one(self, tournament_to_run):
        """This function is the first part of swiss logic.
        list of players in tournament to run is sorted by rank and returned

        Args:
            tournament_to_run (instance): tournament choosen by user

        Returns:
            list: players sorted list
        """

        player_in_tournament_to_run = [
            element[0] for element in sorted(
                tournament_to_run.player_score.items(),
                key=lambda k: (-k[1], k[0].rank))
        ]
        print(player_in_tournament_to_run)
        return player_in_tournament_to_run

    def swiss_logic_sorting_round_two_and_more(self, tournament_to_run):
        """This function is the second part of swiss logic,
        called if a first round already exist. Player are then be sorted by
        score and rank. This function try to avoid matchs who have already
        been played

        Args:
            tournament_to_run (instance): tournament choosen by user

        Returns:
            list: players list sorted
        """
        """
        winner_to_sort = []
        for round in self.round_list[-1].match_list:
            winner_to_sort += round
        """
        """
        c.print(
            "[bold red] *********************\n************\n[bold red]")
        c.print(tournament_to_run.player_score)
        c.print(
            "[bold red] *********************\n*************\n[bold red]")
        """
        player_in_tournament_to_run = [
            element[0] for element in
            sorted(tournament_to_run.player_score.items(),
                   key=lambda k: (-k[1], k[0].rank))]

        """
        c.print(
            "[bold red] *********************\n************\n[bold red]")
        c.print(player_in_tournament_to_run)
        c.print(
            "[bold red] *********************\n************\n[bold red]")
        
        first_list_of_match = []
        for _ in player_in_tournament_to_run:
            first_list_of_match.append(
                [
                    player_in_tournament_to_run[0],
                    player_in_tournament_to_run[1]
                ])
            player_in_tournament_to_run.remove(
                player_in_tournament_to_run[0])
            player_in_tournament_to_run.remove(
                player_in_tournament_to_run[0])

        first_list_of_match.append(
            [
                player_in_tournament_to_run[-2],
                player_in_tournament_to_run[-1]
            ])

        for match_1 in first_list_of_match:
            for match_list in tournament_to_run.tours:
                for match in match_list:
                    if first_list_of_match[-1] == tournament_to_run \
                            .tours[-1][-1]:
                        position = first_list_of_match.index(
                            match_1)
                        player_to_move = first_list_of_match[-1][0]
                        player_to_replace = first_list_of_match[-2][0]
                        first_list_of_match[-2].append(
                            player_to_move)
                        first_list_of_match[-1].append(
                            player_to_replace)

                    else:
                        while match == match_1:
                            position = first_list_of_match.index(
                                match_1)
                            player_to_move = first_list_of_match[
                                position][0]
                            player_to_replace = first_list_of_match[
                                position+1][0]
                            first_list_of_match[
                                position + 1].append(player_to_move)
                            first_list_of_match[
                                position].append(player_to_replace)
                            del (first_list_of_match[position+1][0])
                            del (first_list_of_match[position][0])

        result = []
        for match in first_list_of_match:
            for player in match:
                result.append(player)

        player_in_tournament_to_run = result
        """
        return player_in_tournament_to_run

    def swiss_logic_result(
            self, player_in_tournament_to_run,
            tournament_to_run):
        """This function is the last part of swiss logic. Sorted players list
        is cut in half and ina  loop matchs are created.

        Args:
            player_in_tournament_to_run (list): player sorted
            tournament_to_run (instance): tournament choosen by yser

        Returns:
            instance: tournament choosen with tours attribute filled.
        """

        half_list = len(player_in_tournament_to_run)//2

        first_part = player_in_tournament_to_run[0:half_list]
        # print(first_part)

        second_part = player_in_tournament_to_run[half_list:9]
        # print(second_part)
        ###################################################

        first_list_of_match = []

        for element_1, element_2 in zip(first_part, second_part):
            first_list_of_match.append([element_1, element_2])

        """        serialized_match.append([
                f" {element_1.last_name} {element_1.first_name} == CONTRE ==>"
                f" {element_2.last_name} {element_2.first_name}"])"""

        # add  round list in tournament chosen
        """
        print("OK")
        print(first_list_of_match)
        print("ok")
        """
        match_list = self.match_controller.add_unique_match_list(
            first_list_of_match, tournament_to_run.player_score)

        tournament_to_run.tours.append(match_list.match)

        # c.print(tournament_to_run.tours)

        for tournament in self.started_tournaments:
            if tournament_to_run.name in tournament.name:
                tournament.tours = tournament_to_run.tours

        return tournament_to_run

    def creat_round(self):
        """This function used swiss logic to creat a tour

        Returns:
            instance: tournament instance filled with new tour
        """

        tournament_to_run = self.tournament_view \
            .display_choose_a_tournament_to_launch(
                self.tournament_list, self.round_list)

        if not tournament_to_run:
            return None
        else:
            self.started_tournaments.append(tournament_to_run)

            if len(tournament_to_run.tours) == 4:

                winner_to_sort = []
                for round in self.round_list[-1].match_list:
                    winner_to_sort += round
                c.print(
                    "[bold red] ******************\n************\n[bold red]")
                c.print(tournament_to_run.player_score)
                c.print(
                    "[bold red] ******************\n************\n[bold red]")
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

            if not self.round_list:
                c.print("[bold red]pas encore de round [bold red]\n")

                player_in_tournament_to_run = sorted(
                    tournament_to_run.player_score.keys(),
                    key=lambda k: (k.rank)
                )

                """   elif len(self.round_list) == 0:
                player_in_tournament_to_run = self \
                    .swiss_logic_sorting_round_one(tournament_to_run)"""

                # c.print(tournament_to_run.player_score)

                # continue swiss logic by rank

            elif len(self.round_list) >= 1 and len(self.round_list) < 4:

                player_in_tournament_to_run = self\
                    .swiss_logic_sorting_round_two_and_more(tournament_to_run)

                # print(player_in_tournament_to_run)
                """
                player_in_tournament_to_run = self \
                    .swiss_logic_sorting_round_two_and_more(tournament_to_run)

                match_list = self.match_controller.add_unique_match_list(
                    player_in_tournament_to_run, tournament_to_run.player_score)

                # add first round list in tournament chosen
                tournament_to_run.tours.append(
                    match_list)
                print(tournament_to_run.tours)

                for tournament in self.started_tournaments:
                    if tournament_to_run.name in tournament.name:
                        tournament.tours = tournament_to_run.tours

                """
                """    c.print(
                    "[bold red] *****************\n************\n[bold red]")
                c.print(tournament_to_run.tours[-1])
                c.print(
                    "[bold red] ******************\n************\n[bold red]")
                """

                # return tournament_to_run

        tournament_with_new_round = self.swiss_logic_result(
            player_in_tournament_to_run, tournament_to_run)

        return tournament_with_new_round

    def fill_round_instance_creat_announcement(self):
        """This function use create_round() to creat instance of round
        """

        tournament_running = self.creat_round()
        if not tournament_running in self.tournament_list:
            return None
        else:

            self.round_view.display_round_view(
                tournament_running)

            """
            serialized_match = []
            for match in tournament_running.tours[-1]:
                serialized_match.append([
                    f" {match[0].last_name} {match[0].first_name}"
                    " == CONTRE ==>"
                    f" {match[1].last_name} {match[1].first_name}"])
            """
            # fill round instance with match
            # Check if there is a round else creat round

            if not self.round_list:
                starting_hour = datetime.now()
                self.round_list.append(
                    Round(tournament_running.tours[-1], f"Round {1}",
                          starting_hour,
                          None, 1, tournament_running.name)
                )

                """tournament_tables.update(
                    {"tours":  self.serialized_list_of_tours},
                    query.name == tournament_running.name)"""
            else:
                # if there is a round(s) in list
                # check if there is ending hour else add new round
                # as 2nd  3rd etc..
                match_concerned = len(tournament_running.tours)
                starting_hour = datetime.now()
                self.round_list.append(
                    Round(tournament_running.tours[match_concerned - 1],
                          f"Round {len(self.round_list) + 1}",
                          starting_hour,
                          None, 1, tournament_running.name))

                # self.serialized_list_of_tours = tournament_running \
                # .serialize_tours()
                """
                tournament_tables.update(
                    {"tours":  self.serialized_list_of_tours},
                    query.name == tournament_running.name)"""

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

                if f"{player.last_name} {player.first_name}" == match_list[0][0]:
                    tournament_choice.player_score[player] += 0.5
                    match_list[0][1] += 0.5

                elif f"{player.last_name} {player.first_name}" == match_list[1][0]:
                    tournament_choice.player_score[player] += 0.5
                    match_list[1][1] += 0.5

        elif int(winner_choice) == 0:
            for player in tournament_choice.player_score:
                if f"{player.last_name} {player.first_name}" == match_list[0][0]:
                    tournament_choice.player_score[player] += 1
                    match_list[0][1] += 1

                elif f"{player.last_name} {player.first_name}" == match_list[1][0]:
                    tournament_choice.player_score[player] += 0
                    match_list[1][1] += 0

        elif int(winner_choice) == 1:
            for player in tournament_choice.player_score:
                if f"{player.last_name} {player.first_name}" == match_list[0][0]:
                    tournament_choice.player_score[player] += 0
                    match_list[0][1] += 0

                elif f"{player.last_name} {player.first_name}" == match_list[1][0]:
                    tournament_choice.player_score[player] += 1
                    match_list[1][1] = 1

    def fill_result(self):
        """This function using add_player_point() fill tournament
        instance.player_score and round instance.
        """
        tournament_choice = self.match_view.display_tournament_to_fill_result(
            self.started_tournaments, self.tournament_list, self.round_list)

        round_index = (len(tournament_choice.tours))

        round = tournament_choice.tours[round_index - 1]

        """
        c.print("[bold red]ATTENTION[oold red]")
        print(round)
        """

        for match_list in round:
            winner_choice = self.match_view \
                .display_player_in_tournament_to_fill_score(
                    tournament_choice, match_list)

            self.add_player_point(winner_choice, tournament_choice,
                                  match_list)

            # c.print(tournament_choice)

        for tournament in self.started_tournaments:
            for round in self.round_list:
                if tournament.name == round.tournament_name:
                    if not round.ending_hour:
                        round.ending_hour = datetime.now()

    def report_players_alpahatical_order(self):
        self.tournament_view\
            .report_display_players_in_tournament_by_alphabetical_order(
                self.tournament_list)

    def report_player_by_rank(self):
        self.tournament_view\
            .report_display_players_in_tournament_by_rank(
                self.tournament_list)

    def report_tournament_list(self):
        self.tournament_view.report_display_tournament_list(
            self.tournament_list)

    def report_tour_in_tournament(self):
        self.tournament_view.report_display_tour_in_tournament(
            self.tournament_list, self.round_list)

    def report_match_in_tournament(self):
        self.tournament_view.report_display_match_in_tournament(
            self.tournament_list)

    def report(self):
        """This function using tournament.view.display_report()
        allow acces to report menu.
        """
        '''                        
        self.tournament_view.display_report(
            self.tournament_list, self.round_list, self.unique_match_list,
            self.match_view, self.round_view)
        '''

        if len(self.tournament_list) == 0:
            c.print("[bold red] Vous n'avez aucune données à consulter.[bold red]")
        else:

            secondary_report_menu = {
                "1": {
                    "label": "[bold blue]- 01. Liste de tous les joueurs "
                    "d'un tournoi par ordre alphabétique[bold blue]",
                    "action": self.report_players_alpahatical_order
                },
                "2": {
                    "label": "[bold blue]- 02. Liste de tous les joueurs d'un "
                    "tournoi "
                    "par classement[bold blue]",
                    "action": self.report_player_by_rank
                },
                "3": {
                    "label": "[bold blue]- 03. Liste de tous les tournois."
                    "[bold blue]",
                    "action": self.report_tournament_list
                },
                "4": {
                    "label": "[bold blue]- 04. Liste de tous les tours d'un "
                    "tournoi.[bold blue]",
                    "action": self.report_tour_in_tournament
                },
                "5": {
                    "label": "[bold blue]- 05. Liste de tous les matchs d'un "
                    "tournoi."
                    "[bold blue]",
                    "action": self.report_match_in_tournament
                },

            }

            self.tournament_view.display_report(secondary_report_menu)

    def creat_db(self):
        """This function use db_controller to creat .json file
            If there is no data send appropriate user message.
        """

        self.db.record_data(self.tournament_list, self.player_list,
                            self.db)
        if not self.tournament_list and not self.player_list:
            self.tournament_view.bug_in_db()

    def load_global_player_list(self):
        """this function open .json file and put players from PLAYERS table
        in tournament_controller. It allow user to fill tournament with it

         Returns:
            list: self.player_list in tournament_controller
        """
        try:
            opener = open('db.json')

            data = json.load(opener)

            player_deserializer = []
            index = 0
            for _ in data["PLAYERS"]:
                index += 1
                player_deserializer.append(data["PLAYERS"][str(index)])

            for player in player_deserializer:
                self.player_list.append(Player(
                    player["last_name"],
                    player["first_name"],
                    player["birth"],
                    player["sex"],
                    player["rank"]))

            opener.close()
            return self.player_list
        except FileNotFoundError:
            c.print("[bold red]Vous n'avez pas de base de données[bold red]")
            return None

    def load_player_in_tournament(self, tournament, data):
        """This function will get in database player liste checking index
        to identify the right player and put them in controller
        Args:
            tournament (instance): from a loop of self.tournament_lit
            data (.json): from database .json available
        """
        player_to_get = []
        for player in self.player_list:
            if player.last_name == data["PLAYERS"][
                    str(self.player_list.index(player)+1)]['last_name']:
                player_to_get.append(player)
                for element in self.tournament_list:
                    if tournament["name"] == element.name:
                        element.players = player_to_get

    def load_players_tournament_p_score(self, tournament, data):
        """This function will get player_score in data base identifying player
        with index, and put this dict with player instance as key in controller

        Args:
            tournament (instance): from self.tournement_list loop
            data (.json): from database .json available
        """

        new_dict = {}

        for tournament in self.tournament_list:
            try:
                if tournament.name == data["TOURNAMENT"][
                        str(self.tournament_list.index(tournament)+1)]['name']:
                    for values in data["TOURNAMENT"][
                            str(self.tournament_list.index(tournament)+1)][
                                'player_score'].items():
                        for player in tournament.players:
                            new_dict[player] = values[1]
                    tournament.player_score = new_dict
            except KeyError:
                pass

    def load_touranment(self):
        """This function will load tournament from database in controller
        and allows user to run tournament or uses players already registered

        Returns:
            list: self.tournament_list in tournament_controller
        """

        opener = open('db.json')

        data = json.load(opener)

        tournament_deserializer = []
        index = 0
        for _ in data["TOURNAMENT"]:
            index += 1
            tournament_deserializer.append(data["TOURNAMENT"][str(index)])

        for tournament in tournament_deserializer:
            self.tournament_list.append(Tournament(
                tournament["name"],
                tournament["place"],
                tournament["date"],
                tournament["tours"],
                tournament["players"],
                tournament["time_control"],
                tournament["description"],
                tournament["player_score"]))

            self.load_player_in_tournament(tournament, data)

            self.load_players_tournament_p_score(tournament, data)

        opener.close()
        return self.tournament_list

    def load_data(self):
        """Function used to get player and tournament in tournament controller
        # from .json database
        """

        load_players = self.load_global_player_list()
        if not load_players == self.player_list:
            pass
        else:

            self.load_touranment()

    def generate_data(self):
        """Use this feature to quickly set up a tournament with a list of
        players so you can test the functionality of the program"""

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

        quick_tounarment = [
            Tournament("PARIS Chess-Event", "Paris",
                       datetime.now().strftime("%d-%m-%Y"),
                       [], quick_players_list[0:9], "Blitz",
                       "Description", {}, 4)
        ]

        for tournament in quick_tounarment:
            for player in tournament.players:
                tournament.player_score[player] = 0

        for tournnaments in quick_tounarment:
            self.tournament_list.append(tournnaments)
