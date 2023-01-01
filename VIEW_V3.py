from rich.console import Console

from MODEL_V3 import Players

c = Console()

class MenuView:
    def __init__(self, menu_view ):
        self.menu_view = menu_view

    
    def display_menu_and_get_choice(self):
        c.print("\n[bold yellow] :clipboard: CHESS MENU Veuillez faire un choix "\
            "dans le menu: :clipboard: [bold yellow]\n")
        for element in self.menu_view:
            c.print(self.menu_view[element]["label"])
        menu_choice = c.input("[bold red]==> [bold red]")

        if menu_choice in self.menu_view:
            return self.menu_view[menu_choice]["action"]()
        c.print("\n[bold red]Merci de faire un choix présent"\
                " dans le menu[bold red]\n")
    
    

   

class PlayerView:
    def __init__(self):
        self.players_list = [
            Players("DENIS", "Laurent", "11-12-2000","h",321,0),
            Players("LAURENT", "Denis", "11-10-2005","h",123,0),
            Players("MOINE", "Alice", "10-10-1990","f",100,0),
            Players("VAULT", "Lise", "01-02-1980","f",10,0),
            Players("CREPIN", "Maurice", "12-07-1950","h",40,0),
            Players("TIAGO", "Daniela", "05-06-1977","f",35,0),
            Players("EDON", "Gabrielle", "09-03-1985","f",25,0),
            Players("PATTON", "Gabriel", "09-03-1970","h",20,0)
            ]
    
    def display_players_to_choose(self):
        counter = 0
        value = []
        key = [] 
        
        for players in self.players_list:
            value.append(f"{players.last_name}  {players.first_name}  classement = {players.rank}")
    
        for _ in range(len(value)):
            counter += 1
            key.append(counter)
    
        players_availables = dict(zip(key,value))
        
        c.print("[bold yellow] Liste des joueurs disponibles:\n[bold yellow]")
        for k,v in players_availables.items():
            c.print(f"[bold blue]- {k}: {v}[bold blue]\n")


if __name__ == "__main__":
    PlayerView().display_players_to_choose()