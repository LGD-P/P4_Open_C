from rich.console import Console


from VIEW.player_view import PlayerView
from MODEL.player_model import Player


c = Console()


class PlayerController:
    def __init__(self, player_list):
        self.player_list = player_list
        self.players_list_view = PlayerView()

    def add_player(self):
        """This function get dict from players_list_view.display_player_form()
        and instanced a Player.
        """
        # récupérer le dictionnaire et ajouter un joueur à player list
        player = self.players_list_view.display_player_form()

        self.player_list.append(Player(player["last_name"], player["first_name"],
                                       player["birth"], player["sex"], player["rank"]))

        # print(self.player_list)
