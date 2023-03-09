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
            "date": tournament.date.isoformat(),
            "tours": [],
            "players": [],
            "time_control": tournament.time_control,
            "description": tournament.description,
            "player_score": {}
        }

        return serialized_tournament

    def serialised_tournament_match(self, tournament, round):
        """This function, for each tournament, get match in each round

        Args:
            tournament (instance): in a loop instance of touranment
            round (tuple): tuple of tow list

        Returns:
            _type_: _description_
        """
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

    def serialised_tournament_tours(self, tournament):
        """This function allow to serialize class Round as
                Tournament().tours

                Args:
                    tournament (instance): tournament in a loop of global tournament list
                    table_tournament (json table): TOURNAMENT table

                """

        if not tournament.tours:
            return None
        else:

            serialized_tournament_tour = []

            for round in tournament.tours:
                serialized_tournament_tour.append({
                    "tournament_name":
                    round.tournament_name,
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
        return serialized_tournament_tour

    def serialize_players_in_tournament(self, tournament):
        """This function get player in tournament compare to
        global player list

        Args:
            tournament (instance): tournament in a loop of global tournament list

        Returns:
            list: index of each player compare to global player list
        """

        global_player_list = []
        for player in self.player_list:
            global_player_list.append(str(self.player_list.index(player) + 1))

        player_list_index = [
            index + 1 for (index, player) in enumerate(tournament.players)
        ]

        return player_list_index

    def serialize_player_score(self, tournament):
        """This function get player score

        Args:
            tournament (instance): tournament in a loop of global tournament list

        Returns:
            dict : index player as key and score as value
        """
        player_score_dict = {}
        player_index = []
        player_score = []

        if tournament.players != []:
            for player in tournament.players:
                player_index.append(str(tournament.players.index(player) + 1))
            for p_score in tournament.player_score:
                player_score.append(tournament.player_score[p_score])

                player_score_dict = dict(zip(player_index, player_score))

        return player_score_dict

    def serialize_players_in_player_list(self, player):
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
            'birth': player.birth.isoformat(),
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
                table_players.insert(self.serialize_players_in_player_list(player))

        if not tournament_list:
            pass
        else:
            for tournament in tournament_list:
                table_tournament.insert(self.serialised_tournament(tournament))
                if tournament.players != []:
                    table_tournament.update(
                        {"players": self.serialize_players_in_tournament(tournament)},
                        where("name") == tournament.name)
                    table_tournament.update(
                        {"player_score": self.serialize_player_score(tournament)},
                        where("name") == tournament.name)

                if tournament.tours != []:
                    table_tournament.update(
                        {"tours": self.serialised_tournament_tours(tournament)},
                        where('name') == tournament.name)

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
                    Player(player["last_name"], player["first_name"], datetime.fromisoformat(player["birth"]),
                           player["sex"], player["rank"]))

            opener.close()
            return self.player_list
        except FileNotFoundError:
            ErrorAndUserMessages().bug_cannot_load_db()
            return None

    def load_players_in_tournament(self, tournament, data):
        """This function load players in each tournament

        Args:
            tournament (instance): tournament in a loop of global tournament list
            data (.json db): PLAYERS table

        Returns:
            list: list of player instance
        """
        player_in_tournament_as_index = []
        for players in tournament["players"]:
            player_in_tournament_as_index.append(players)

        players_to_get = []
        for player in data["PLAYERS"]:
            players_to_get.append(
                Player(data["PLAYERS"][str(player)]["last_name"],
                       data["PLAYERS"][str(player)]["first_name"],
                       datetime.fromisoformat(data["PLAYERS"][str(player)]["birth"]),
                       data["PLAYERS"][str(player)]["sex"],
                       data["PLAYERS"][str(player)]["rank"]))

        player_to_put_in_tournament = []
        for player in players_to_get:
            if players_to_get.index(player) + 1 in player_in_tournament_as_index:
                player_to_put_in_tournament.append(player)

        return player_to_put_in_tournament

    def load_players_tournament_p_score(self, tournament):
        """This function will load player_score in data base identifying player
                with index, and put this dict with player instance as key in controller

                Args:
                    tournament (instance): from self.tournement_list loop
                    data (.json): from database .json available
                """

        players = [player for player in self.player_list]
        score = []

        for value in tournament['player_score'].values():
            score.append(value)
        players_score = dict(zip(players, score))

        return players_score

    def load_match_list_in_round(self, tours, data):
        """This function load match list, to be used in Round()

        Args:
            tours (instance): instance of Round() in Tournament()
            data (.json): touranment_table

        Returns:
            list1: match list for each round
        """
        match_list_loaded = []

        for player in tours["match_list"]:

            match_list_loaded.append(([
                Player(data["PLAYERS"][str(player[0][0]['joueur'])]["last_name"],
                       data["PLAYERS"][str(player[0][0]['joueur'])]["first_name"],
                       datetime.fromisoformat(data["PLAYERS"][str(player[0][0]['joueur'])]["birth"]),
                       data["PLAYERS"][str(player[0][0]['joueur'])]["sex"],
                       data["PLAYERS"][str(player[0][0]['joueur'])]["rank"]),
                player[0][1]["score"]
            ], [
                Player(data["PLAYERS"][str(player[1][0]['joueur'])]["last_name"],
                       data["PLAYERS"][str(player[1][0]['joueur'])]["first_name"],
                       datetime.fromisoformat(data["PLAYERS"][str(player[1][0]['joueur'])]["birth"]),
                       data["PLAYERS"][str(player[1][0]['joueur'])]["sex"],
                       data["PLAYERS"][str(player[1][0]['joueur'])]["rank"]),
                player[1][1]["score"]
            ]))

        return match_list_loaded

    def load_tours_in_tournament(self, tournament, data):
        """This function all to deserialise Round() from db

                Args:
                    tournament_deserializer (list): Tournament from TOURNAMENT table

                Returns:
                    list: List of Round()
                """

        tours_in_tournament = []

        if tournament["tours"] == []:
            return None

        if tournament["name"] == tournament["tours"][0]["tournament_name"]:

            for tours in tournament["tours"]:

                match_list = self.load_match_list_in_round(tours, data)
                if tours["ending_hour"] == "None":
                    tours_in_tournament.append(
                        Round(
                            match_list, tours["name"],
                            datetime.strptime(tours['starting_hour'][0:19],
                                              '%Y-%m-%d  %H:%M:%S'), None,
                            tours["number_of_round"], tours["tournament_name"]))

                else:

                    tours_in_tournament.append(
                        Round(
                            match_list, tours["name"],
                            datetime.strptime(tours['starting_hour'][0:19],
                                              '%Y-%m-%d  %H:%M:%S'),
                            datetime.strptime(tours['ending_hour'][0:19],
                                              '%Y-%m-%d  %H:%M:%S'),
                            tours["number_of_round"], tours["tournament_name"]))

        return tours_in_tournament

    def load_first_tournament_part(self, tournament):
        """This function load a tournament if there is no Players in it.
        so no round no players socre.

        Args:
            tournament (instance): instance of Tournament in .json file
        """

        self.tournament_list.append(
            Tournament(tournament["name"], datetime.fromisoformat(tournament["date"]), tournament["place"],
                       [], [], tournament["time_control"],
                       tournament["description"], {}))

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

            if tournament["players"] != [] and tournament["tours"] == []:
                self.tournament_list.append(
                    Tournament(tournament["name"], datetime.fromisoformat(tournament["date"]),
                               tournament["place"], [],
                               self.load_players_in_tournament(tournament, data),
                               tournament["time_control"], tournament["description"],
                               self.load_players_tournament_p_score(tournament)))

            elif tournament["tours"] != []:
                self.tournament_list.append(
                    Tournament(
                        tournament["name"], datetime.fromisoformat(tournament["date"]), tournament["place"],
                        self.load_tours_in_tournament(tournament, data),
                        self.load_players_in_tournament(tournament, data),
                        tournament["time_control"], tournament["description"],
                        self.load_players_tournament_p_score(tournament)))

            elif tournament["players"] == []:

                self.load_first_tournament_part(tournament)

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
