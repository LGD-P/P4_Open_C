from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Tournament:
    name : str
    date : str
    place : str
    tours : list
    players : list
    time_control : str
    description : str
    number_of_rounds : int = 4
    
    def __post_init__(self):
        self.display_tournament =  (f"- Nom du tounois: {self.name}\n"
                                    f"- Date du tournois: {self.date}\n"
                                    f"- Lieu du tournois: {self.place}\n"
                                    f"- Nombre de round: {self.number_of_rounds}\n"
                                    f"- Liste des tours: {self.tours}\n"
                                    f"- Liste des joueurs: {self.players}\n"
                                    f"- Mode de contrôle du temps: {self.time_control}\n"
                                    f"- Description: {self.tours}\n"
                                    )

@dataclass
class Player:
    first_name : str
    last_name : str
    birth : str
    sex : str
    rank : int
    counter : ClassVar[int] = 0
 

    def __post_init__(self):
        Player.counter += 1
        self.display_player = (f"- Nom: {self.first_name}\n"
                               f"- Prénom: {self.last_name}\n"
                               f"- Date de naissance: {self.birth}\n"
                               f"- Sexe: {self.sex}\n"
                               f"- rank: {self.rank}\n"
                               )
    

premier_tournois = Tournament("Paris_Game_Show", 
                              "12-12-2022", 
                              "Paris",
                              [],
                              [],
                              "Bullet",
                              "C'est LE tournois"
                              )
                                  
                                  
                                  
player_1 = Player("Martin",
                   "Philippe",
                   "12-10-1980",
                   "M",
                   113)

player_2 = Player("Durand",
                   "Denise",
                   "12-12-1985",
                   "M",
                   120)


                         
                                  
print(premier_tournois.display_tournament)
   
print(f"Le nom de joueur créé est {Player.counter}")
    