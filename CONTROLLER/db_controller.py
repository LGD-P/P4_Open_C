from tinydb import TinyDB, Query, where


query = Query()


class DataBase:

    def creat_data_base(self):
        db = TinyDB('db.json', indent=4, encoding='utf-8')
        # player_table = db.table("PLAYERS")

        return db

    def serialised_tournament(self, tournament):

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

        table_tournament.upsert(
            {"player_score": player_score_dict_in_tournament_table}, where("player_score") == {})

    def serialize_players(self, player):

        serialized_players = {
            'last_name': player.last_name,
            'first_name': player.first_name,
            'birth': player.birth,
            'sex': player.sex,
            'rank': player.rank
        }

        return serialized_players

    def record_data(self, tournament_list, player_list, db):

        db = self.creat_data_base()
        # db.drop_table("_default")
        while not tournament_list or not player_list:
            return None

        table_tournament = db.table("TOURNAMENT")
        table_tournament.truncate()
        table_players = db.table("PLAYERS")
        table_players.truncate()

        for player in player_list:
            table_players.insert(self.serialize_players(player))

        for tournament in tournament_list:
            table_tournament.insert(self.serialised_tournament(tournament))

        self.serialized_player_and_score_in_t_table(
            tournament_list, table_tournament)
