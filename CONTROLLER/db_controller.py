from tinydb import TinyDB, Query, where


query = Query()


class DataBase:

    def creat_data_base(self):
        db = TinyDB('db.json', indent=4, encoding='utf-8')
        # player_table = db.table("PLAYERS")

        return db

    def record_tournament(self, tournament_list, db):

        db = self.creat_data_base()
        db.truncate()
        table_tournament = db.table("TOURNAMENT")

        for tournament in tournament_list:
            serialized_tournament = {
                "name": tournament.name,
                "place": tournament.place,
                "date": tournament.date,
                "tours": tournament.tours,
                "players": [],
                "time_control": tournament.time_control,
                "description": tournament.description,
                # "player_score": tournament.player_score
            }

        table_tournament.truncate()
        table_tournament.insert(serialized_tournament)

        player_list_index = []
        for tournament in tournament_list:
            for player in tournament.players:
                player_list_index.append(tournament.players.index(player))

        table_tournament.update({
            "players": player_list_index}, where('players') == [])


if __name__ == "__main__":
    print("ok")


"""
players_tables.insert(serialized_player)
tournament_tables.insert(serialized_tournament)

tournament_tables.update(
    {
        "players":  self.serialized_list_of_players
    }, query.name == tournament.name)

tournament_tables.update(
    {
        "player_score":  self.serialized_list_of_score
    }, query.name == tournament.name)


serialized_player = player.serialized_player()

self.serialized_list_of_players.append(serialized_player)

self.serialized_list_of_score = tournament.serialize_player_score(
    player)

c.print(self.serialized_list_of_score)


self.serialized_list_of_tours.append(serialized_match)
# c.print(tournament_to_run.player_score)


serialized_match = []
            for match in tournament_running.tours[-1]:
                serialized_match.append([
                    f" {match[0].last_name} {match[0].first_name}"
                    " == CONTRE ==>"
                    f" {match[1].last_name} {match[1].first_name}"])

tournament_tables.update(
    {"tours":  self.serialized_list_of_tours},
    query.name == tournament_running.name)


tournament_tables.update(
    {"player_score":  self.serialized_list_of_score},
    query.name == tournament_choice.name)


self.serialized_list_of_score[
                        f"{player.last_name}, {player.first_name}"] += 0
  self.serialized_list_of_score[
                        f"{player.last_name}, {player.first_name}"] += 1


 for tournament in quick_tounarment:
            serialize_tournament.append({
                "name": tournament.name,
                "date": tournament.date,
                "place": tournament.place,
                "tours": tournament.tours,
                "time_control": tournament.time_control,
                "description": tournament.description,
            })
        serialize_tournament = []
        for tournament in serialize_tournament:
            tournament_tables.insert(tournament)

        serialize_player = []

        self.serialized_list_of_score = {}
        tournament = quick_tounarment[0].name

        for player in quick_players_list:
            serialize_player.append(
                {"last_name": player.last_name,
                 "first_name": player.first_name,
                 "birth": player.birth,
                 "sex": player.sex,
                 "rank": player.rank
                 })

            self.serialized_list_of_score[
                f"{player.last_name}, {player.first_name}"] = 0

        for player in serialize_player:
            players_tables.insert(player)

        tournament_tables.update(
            {
                "player":  serialize_player,

            }, query.name == tournament)

        tournament_tables.update(
            {
                "player_score":  self.serialized_list_of_score,

            }, query.name == tournament)
"""
