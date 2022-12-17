from dataclasses import dataclass
from typing import ClassVar


@dataclass
class Tournament:
    name: str
    date: str
    place: str
    tours: list
    players: list
    time_control: str
    description: str
    number_of_rounds: int = 4


    def __post_init__(self):
        self.display_tournament = (f"\n- Nom du tounois: {self.name}\n"
                                   f"- Date du tournois: {self.date}\n"
                                   f"- Lieu du tournois: {self.place}\n"
                                   f"- Nombre de round: {self.number_of_rounds}\n"
                                   f"- Liste des tours: {self.tours}\n"
                                   f"- Liste des joueurs: {self.players}\n"
                                   f"- Mode de contrôle du temps: {self.time_control}\n"
                                   f"- Description: {self.description}\n"
                                   )


@dataclass
class Players:
    last_name: str
    first_name: str  
    birth: str
    sex: str
    rank: int
    points: int = 6548



    def __post_init__(self):
        self.display_player = (f"- Nom: {self.last_name}\n"
                               f"- Prénom: {self.first_name}\n"
                               f"- Date de naissance: {self.birth}\n"
                               f"- Sexe: {self.sex}\n"
                               f"- rank: {self.rank}\n"
                               f"- points: {self.points}\n"
                               )
        


@dataclass
class Rounds:
    matching_lists : list
    players_names: "Players.first_name , Players.last_name"
    starting_match_time: str
    end_match_time: str
    
    
@dataclass
class Match:
    list_of_mach_tuples: list
    
    