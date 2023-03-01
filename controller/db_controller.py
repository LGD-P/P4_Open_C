from rich.console import Console
import json
from tinydb import TinyDB, where
from datetime import datetime

from model.tournament_model import Tournament
from model.player_model import Player
from model.round_model import Round

from view.error_and_user_messages import ErrorAndUserMessages

c = Console()


class DataBase:

    def __init__(self, player_list, tournament_list):
        self.player_list = player_list
        self.tournament_list = tournament_list

    def creat_data_base(self):
        """This function creats json file for future data

            Returns:
                .json_: .json file to record data in
            """
        db = TinyDB('db.json', indent=4, encoding='utf-8')

        return db

    def serialised_tournament_match(self, tournament, round):
        player_index = [(tournament.players.index(player) + 1)
                        for player in tournament.players]

        dict_for_match = {
            str(player): index
            for player, index in zip(tournament.players, player_index)
        }

        match_list_of_round = []
        for player in round.match_list:
            match_list_of_round.append(([{
                'joueur': dict_for_match[str(player[0][0])]
            }, {
                'score': player[0][1]
            }], [{
                'joueur': dict_for_match[str(player[1][0])]
            }, {
                'score': player[1][1]
            }]))

        return match_list_of_round

    def serialised_tournament_tours(self, tournament, table_tournament):
        """This function allow to serialize class Round as
            Tournament().tours

            Args:
                tournament (instance): tournament
                table_tournament (json table): TOURNAMENT table

            """

        if not tournament.tours:
            return None
        else:

            serialized_tournament_tour = []

            for round in tournament.tours:
                serialized_tournament_tour.append({
                    "tournament_name":
                    round.name,
                    "name":
                    round.name,
                    "starting_hour":
                    str(round.starting_hour),
                    "ending_hour":
                    str(round.ending_hour),
                    "number_of_round":
                    round.number_of_round,
                    "match_list":
                    self.serialised_tournament_match(tournament, round)
                })

            table_tournament.update({"tours": serialized_tournament_tour})

    def serialised_tournament(self, tournament):
        """This function will be used in a loop
            to put all tournaments recorded in data base

            Args:
                tournament (tournament): instance of tournament

            Returns:
                dict: dict of a tournament
            """

        serialized_tournament = {
            "name": tournament.name,
            "place": tournament.place,
            "date": tournament.date,
            "tours": None,
            "players": [],
            "time_control": tournament.time_control,
            "description": tournament.description,
            "player_score": {}
        }
        return serialized_tournament

    def serialized_player_and_score_in_t_table(self, table_tournament):
        """this function will be specificly used to fill player_score and
            list of player in tournament. To identify player, this function uses
            index of players_table

            Args:
                tournament_list (list): list of each touranment
                table_tournament (dict): tournament table in .json file
            """
        player_list_index = []
        player_score_dict_in_tournament_table = {}

        for tournament in self.tournament_list:
            if tournament.players != []:
                for player in tournament.players:
                    player_list_index.append(
                        tournament.players.index(player) + 1)
                    player_score_dict_in_tournament_table[
                        tournament.players.index(player) + 1] = tournament.player_score[player]

                table_tournament.upsert({"players": player_list_index},
                                        where('players') == [])

                table_tournament.upsert(
                    {"player_score": player_score_dict_in_tournament_table},
                    where("player_score") == {})
            else:
                pass

    def serialize_players(self, player):
        """This function will be used in a loop
            to put all players recorded in data base

            Args:
                player (instance): from tournament.players

            Returns:
                dict : dict of a player
            """

        serialized_players = {
            'last_name': player.last_name,
            'first_name': player.first_name,
            'birth': player.birth,
            'sex': player.sex,
            'rank': player.rank
        }

        return serialized_players

    def save_data(self, tournament_list, player_list):
        """This function uses previous ones to record all data
            in .json file


            Args:
                tournament_list (list): list of each touranment
                player_list (_type_): list of each player
                db (.json): .json file created

            Returns:
                _type_: _description_
            """

        db = self.creat_data_base()

        if not tournament_list and not player_list:
            return None

        table_tournament = db.table("TOURNAMENT")
        table_tournament.truncate()
        table_players = db.table("PLAYERS")
        table_players.truncate()

        if not player_list:
            pass
        else:
            for player in player_list:
                table_players.insert(self.serialize_players(player))

        if not tournament_list:
            pass
        else:
            for tournament in tournament_list:
                table_tournament.insert(self.serialised_tournament(tournament))
                self.serialised_tournament_tours(tournament, table_tournament)
                if tournament.players != []:
                    self.serialized_player_and_score_in_t_table(table_tournament)

    def creat_db(self):
        """This function use db_controller to creat .json file
                If there is no data send appropriate user message.
            """

        if not self.tournament_list and not self.player_list:
            ErrorAndUserMessages().bug_to_creat_db()
        else:
            self.save_data(self.tournament_list, self.player_list)
        ErrorAndUserMessages().database_created()

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
                self.player_list.append(
                    Player(player["last_name"], player["first_name"], player["birth"],
                           player["sex"], player["rank"]))

            opener.close()
            return self.player_list
        except FileNotFoundError:
            ErrorAndUserMessages().bug_cannot_load_db()
            return None

    def load_player_in_tournament(self, data):
        """This function will get in database player liste checking index
            to identify the right player and put them in controller
            Args:
                tournament (instance): from a loop of self.tournament_lit
                data (.json): from database .json available
            """
        player_to_get = []
        for player in data["PLAYERS"]:
            if player:

                player_to_get.append(
                    Player(data["PLAYERS"][str(player)]["last_name"],
                           data["PLAYERS"][str(player)]["first_name"],
                           data["PLAYERS"][str(player)]["birth"],
                           data["PLAYERS"][str(player)]["sex"],
                           data["PLAYERS"][str(player)]["rank"]))
                for tournament_to_fill in self.tournament_list:
                    if data["TOURNAMENT"][str(
                        self.tournament_list.index(tournament_to_fill) + 1)]["name"] == tournament_to_fill\
                            .name:
                        tournament_to_fill.players = player_to_get

    def load_players_tournament_p_score(self, tournament, data):
        """This function will get player_score in data base identifying player
            with index, and put this dict with player instance as key in controller

            Args:
                tournament (instance): from self.tournement_list loop
                data (.json): from database .json available
            """

        new_dict = {}
        index = -1

        for tournament in self.tournament_list:
            try:
                if tournament.name == data["TOURNAMENT"][str(
                        self.tournament_list.index(tournament) + 1)]['name']:
                    for values in data["TOURNAMENT"][str(
                            self.tournament_list.index(tournament) + 1)]['player_score'].items():
                        index += 1
                        new_dict[tournament.players[index]] = values[1]
                    tournament.player_score = new_dict

            except KeyError:
                pass

    def load_match_list_in_round(self, tours, data):
        match_list_loaded = []

        for player in tours["match_list"]:

            match_list_loaded.append(([
                Player(data["PLAYERS"][str(player[0][0]['joueur'])]["last_name"],
                       data["PLAYERS"][str(
                           player[0][0]['joueur'])]["first_name"],
                       data["PLAYERS"][str(player[0][0]['joueur'])]["birth"],
                       data["PLAYERS"][str(player[0][0]['joueur'])]["sex"],
                       data["PLAYERS"][str(player[0][0]['joueur'])]["rank"]),
                player[0][1]["score"]
            ], [
                Player(data["PLAYERS"][str(player[1][0]['joueur'])]["last_name"],
                       data["PLAYERS"][str(
                           player[1][0]['joueur'])]["first_name"],
                       data["PLAYERS"][str(player[1][0]['joueur'])]["birth"],
                       data["PLAYERS"][str(player[1][0]['joueur'])]["sex"],
                       data["PLAYERS"][str(player[1][0]['joueur'])]["rank"]),
                player[1][1]["score"]
            ]))

        return match_list_loaded

    def load_tours_in_tournament(self, tournament_deserializer, data):
        """This function all to deserialise Round() from db

            Args:
                tournament_deserializer (list): Tournament from TOURNAMENT table

            Returns:
                list: List of Round()
            """

        deserialized_tournament = []

        for tournament in tournament_deserializer:
            if not tournament["tours"]:
                return None
            else:
                for tours in tournament["tours"]:
                    match_list = self.load_match_list_in_round(tours, data)
                    if tours["ending_hour"] == "None":
                        deserialized_tournament.append(
                            Round(
                                match_list, tours["name"],
                                datetime.strptime(tours['starting_hour'][0:19],
                                                  '%Y-%m-%d  %H:%M:%S'), None,
                                tours["number_of_round"], tours["tournament_name"]))

                    else:

                        deserialized_tournament.append(
                            Round(
                                match_list, tours["name"],
                                datetime.strptime(tours['starting_hour'][0:19],
                                                  '%Y-%m-%d  %H:%M:%S'),
                                datetime.strptime(tours['ending_hour'][0:19],
                                                  '%Y-%m-%d  %H:%M:%S'),
                                tours["number_of_round"], tours["tournament_name"]))

            return deserialized_tournament

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

        # tours = self.load_tours_in_tournament(
        #  tournament_deserializer, data)

        for tournament in tournament_deserializer:
            if tournament["players"] != []:
                self.tournament_list.append(
                    Tournament(
                        tournament["name"], tournament["date"], tournament["place"],
                        self.load_tours_in_tournament(
                            tournament_deserializer, data),
                        tournament["players"], tournament["time_control"],
                        tournament["description"], tournament["player_score"]))

                self.load_player_in_tournament(data)

                self.load_players_tournament_p_score(tournament, data)
            else:

                self.tournament_list.append(
                    Tournament(
                        tournament["name"], tournament["date"], tournament["place"],
                        tournament["tours"], tournament["players"], tournament["time_control"],
                        tournament["description"], tournament["player_score"]))

        opener.close()
        return self.tournament_list

    def load_data(self):
        """Function used to get player and tournament in tournament controller
            # from .json database
            """
        self.player_list.clear()
        self.tournament_list.clear()

        load_players = self.load_global_player_list()
        if not load_players == self.player_list:
            pass
        else:

            self.load_touranment()
            ErrorAndUserMessages().database_loaded()
