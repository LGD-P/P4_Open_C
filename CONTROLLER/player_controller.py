from rich.console import Console


from VIEW.player_view import PlayerView



c = Console()  


class PlayerController:
    def __init__(self, player_list):
        self.player_list = player_list
        self.players_list_controller = PlayerView()

    def add_player(self):
      self.player_list.append(self.players_list_controller.display_player_form())
      # print de debug
      print(self.player_list)
        

        
            