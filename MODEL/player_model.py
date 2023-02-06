from rich.console import Console
c = Console()


class Player:
    def __init__(self, last_name: str, first_name: str,
                 birth: str, sex: str, rank: int):

        self.last_name = last_name
        self.first_name = first_name
        self.birth = birth
        self.sex = sex
        self.rank = rank

    def __str__(self):
        return (f"- Nom: {self.last_name}\n"
                f"- Prénom: {self.first_name}\n"
                f"- Date de naissance: {self.birth}\n"
                f"- Sexe: {self.sex}\n"
                f"- rank: {self.rank}\n"
                )

    def __repr__(self):
        return (f"\n- Nom : {self.last_name}"
                f" Prénom : {self.first_name} "
                f" Date de naissance : {self.birth} "
                f" Sexe : {self.sex} "
                f" rank : {self.rank} ")

    def serialized_player(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "birth": self.birth,
            "sex": self.sex,
            "sank": self.rank
        }
