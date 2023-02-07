

class Tournament:
    def __init__(self, name: str, date: str, place: str, tours: list,
                 players: list, time_control: str, description: str,
                 player_score: dict, number_of_rounds: int = 4):
        self.name = name
        self.date = date
        self.place = place
        self.tours = tours
        self.players = players
        self.time_control = time_control
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.player_score = player_score

    def __str__(self):
        return (
            f"\n- Nom du tounois: {self.name}\n"
            f"- Date du tournois: {self.date}\n"
            f"- Lieu du tournois: {self.place}\n"
            f"- Nombre de round: {self.number_of_rounds}\n"
            f"- Liste des tours: {self.tours}\n"
            f"- Liste des joueurs: {self.players}\n"
            f"- Mode de contrôle du temps: {self.time_control}\n"
            f"- Description: {self.description}\n"
            f"- Nombre de round: {self.number_of_rounds}\n"
            f"- Score des joueurs:{self.player_score}\n")

    def __repr__(self):
        return (
            f"\n- Nom du tounois: {self.name}\n"
            f"- Date du tournois: {self.date}\n"
            f"- Lieu du tournois: {self.place}\n"
            f"- Nombre de round: {self.number_of_rounds}\n"
            f"- Liste des tours: {self.tours}\n"
            f"- Liste des joueurs: {self.players}\n"
            f"- Mode de contrôle du temps: {self.time_control}\n"
            f"- Nombre de round: {self.number_of_rounds}\n"
            f"- Score des joueurs :{self.player_score}\n")

    def serialize_player_score(self, player):
        serialize_score = {}
        for player in self.players:
            serialize_score[f"{player.last_name}, {player.first_name}"] = 0
        return serialize_score
