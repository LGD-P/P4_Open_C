from rich.console import Console
from datetime import datetime
c = Console()


class Player:
    def __init__(self, last_name: str, first_name: str,
                 birth: datetime, sex: str, rank: int):

        self.last_name = last_name
        self.first_name = first_name
        self.birth = birth
        self.sex = sex
        self.rank = rank

    def __str__(self):
        return (f"- Nom: {self.last_name} "
                f"- Prénom: {self.first_name} "
                f"- Date de naissance: {self.birth.strftime('%d/%m/%Y')} "
                f"- Sexe: {self.sex} "
                f"- rank: {self.rank}"
                )

    def __repr__(self):
        return (f"\n- Nom : {self.last_name}"
                f" Prénom : {self.first_name} "
                f" Date de naissance : {self.birth.strftime('%d/%m/%Y')} "
                f" Sexe : {self.sex} "
                f" rank : {self.rank} ")

    def serialized_player(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth": {datetime.strftime(self.birth, '%d/%m/%Y')},
            "sex": self.sex,
            "sank": self.rank
        }
