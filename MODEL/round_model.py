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
