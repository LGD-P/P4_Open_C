from dataclasses import dataclass


@dataclass
class Round:
    match_list: list
    name: str
    date: str
    starting_hour: str
    ending_hour: str
    number_of_round: str
    tournament_name: str


"""En plus de la liste des correspondances, chaque instance du tour doit contenir
un champ de nom. Actuellement, nous appelons nos tours "Round 1", "Round 2", etc.
Elle doit également contenir un champ Date et heure de début et un champ 
Date et heure de fin, qui doivent tous deux être automatiquement remplis lorsque 
l'utilisateur crée un tour et le marque comme terminé. 

Les instances de round doivent être stockées dans une liste sur l'instance de tournoi
à laquelle elles appartiennent."""
