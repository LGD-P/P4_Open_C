from dataclasses import dataclass


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
