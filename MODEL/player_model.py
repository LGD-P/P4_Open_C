from dataclasses import dataclass


@dataclass
class Player:
    last_name: str
    first_name: str
    birth: str
    sex: str
    rank: int

    def __post_init__(self):
        self.display_player = (f"- Nom: {self.last_name}\n"
                               f"- Prénom: {self.first_name}\n"
                               f"- Date de naissance: {self.birth}\n"
                               f"- Sexe: {self.sex}\n"
                               f"- rank: {self.rank}\n"

                               )
