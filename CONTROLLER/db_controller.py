from pathlib import Path
import json
from tinydb import TinyDB, where


class DataBase:

    def creat_data_base(self):
        """This function creats json file for future data

        Returns:
            .json_: .json file to record data in
        """
        db = TinyDB('db.json', indent=4, encoding='utf-8')
        # player_table = db.table("PLAYERS")

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
            "date": tournament.date,
            "tours": tournament.tours,
            "players": [],
            "time_control": tournament.time_control,
            "description": tournament.description,
            "player_score": {}
        }
        return serialized_tournament

    def serialized_player_and_score_in_t_table(self, tournament_list, table_tournament):
        """this function will be specificly used to fill player_score and 
        list of player in tournament. To identify player, this function uses
        index of players_table

        Args:
            tournament_list (list): list of each touranment
            table_tournament (dict): tournament table in .json file
        """
        player_list_index = []
        player_score_dict_in_tournament_table = {}

        for tournament in tournament_list:
            for player in tournament.players:
                player_list_index.append(
                    tournament.players.index(player)+1)
                player_score_dict_in_tournament_table[tournament.players.index(
                    player)+1] = tournament.player_score[player]

        table_tournament.upsert({
            "players": player_list_index}, where('players') == [])

        if not tournament_list:
            pass
        else:
            table_tournament.upsert(
                {"player_score": player_score_dict_in_tournament_table}, where("player_score") == {})

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

    def record_data(self, tournament_list, player_list, db):
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
        # db.drop_table("_default")
        while not tournament_list and not player_list:
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

            if not player_list:
                pass
            else:
                self.serialized_player_and_score_in_t_table(
                    tournament_list, table_tournament)
