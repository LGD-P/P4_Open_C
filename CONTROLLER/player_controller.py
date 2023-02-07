from rich.console import Console
from tinydb import TinyDB

from VIEW.player_view import PlayerView
from MODEL.player_model import Player


c = Console()

db = TinyDB('db.json', indent=4, encoding='utf-8')

players_tables = db.table("PLAYERS")
players_tables.truncate()


class PlayerController:
    def __init__(self, player_list):
        self.player_list = player_list
        self.players_list_view = PlayerView()

    def add_player(self):
        """This function get dict from players_list_view.display_player_form()
        and instanced a Player, then add player data in database
        """
        # récupérer le dictionnaire et ajouter un joueur à player list
        serialized_player = self.players_list_view.display_player_form()

        player_instance = Player(
            serialized_player["last_name"],
            serialized_player["first_name"],
            serialized_player["birth"],
            serialized_player["sex"],
            serialized_player["rank"])

        self.player_list.append(player_instance)

        players_tables.insert(serialized_player)
        # print(self.player_list)
