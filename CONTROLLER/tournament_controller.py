from rich.console import Console


from VIEW.tournament_view import TournamentView
from VIEW.player_view import PlayerView


c = Console()  

      
class TournamentController:
    def __init__(self,tournament_list, player_list) :
           self.tournament_view = TournamentView()
           self.tournament_list = tournament_list
           self.player_view = PlayerView()
           self.player_list = player_list
           
           
    def add_tournament(self):
         self.tournament_list.append(self.tournament_view.display_tournament_form())
         # prin de débug
         print(self.tournament_list)
 
   
   
     
    def add_player_in_tournament(self):
        
        if not self.tournament_list :
            
            c.print("[bold red]Veuillez créer un tournois pour "\
                "pouvoir l'alimenter en joueurs..\n [bold red]")
            
        elif not self.player_list:
            c.print("[bold red]Veuillez créer des joueurs pour "\
            "pouvoir les ajouter à des tournois")
            
        else:
            
            c.print("[bold yellow]Choisissez un tournois dans lequel"\
                " ajouter un joueur: [bold yellow]")
            
            propose_tournament = self.tournament_view.display_tournament(self.tournament_list)
                  
            tournament_choice = c.input("[bold red]==>[bold red]")
            
            while not tournament_choice.isdigit() or not int(tournament_choice) in propose_tournament:
                c.print("[bold red] Faites un choix dans la liste[bold red]")
                tournament_choice = c.input("[bold red]==>[bold red]")
                
            tournament_choice = self.tournament_list[int(tournament_choice)]
                
            
            propose_players = self.player_view.display_players_to_choose(self.player_list, tournament_choice.players)
            # afficher seulement les joueurs qui ne sont pas dans le tournois 

            
            if type(propose_players) == dict:
                player_choice = c.input(
                    "[bold yellow]Entrez le N° correspondant à votre choix [blod yellow]"
                    )
          
            
                while not player_choice.isdigit() or not int(player_choice) in propose_players:
                    c.print("[bold red] Faites un choix dans la liste[bold red]")
                    player_choice = c.input(
                        "[bold red]==> [blod red]"
                        )
                
                player_choice = self.player_list[int(player_choice)]
                # n'afficher que les players qui ne sont pas déjà dans les tournois.
                while player_choice in tournament_choice.players :
                    c.print("[bold red] Ce joueur est déjà dans le tournois merci d'en choisir un autre[bold red]")
                    player_choice = c.input(
                        "[bold red]==> [blod red]"
                        )
                    
            
                tournament_choice.players.append(player_choice)
                                
                print("****"*10)
                print("Affichage du tournois après alimentation: \n")
                print(tournament_choice)
            
            else:
                pass


        
          
          
          
