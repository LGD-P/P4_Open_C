

class Round:
    def __init__(self, match_list: list, name: str,
                 starting_hour: str, ending_hour: str,
                 number_of_round: str, tournament_name: str):

        self.match_list = match_list
        self.name = name
        self.starting_hour = starting_hour
        self.ending_hour = ending_hour
        self.number_of_round = number_of_round
        self.tournament_name = tournament_name

    def __str__(self):
        return f"- {self.name}\n"\
            f"- Début de round : {self.starting_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n"\
            f"- Fin de round : {self.ending_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n"\
            f"- Liste des match: {self.match_list}\n"

    def __repr__(self):
        return f"{self.tournament_name}\n"\
               f"{self.name}\n"\
               f"{self.starting_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n"\
               f"{self.ending_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n"\
               f"{self.number_of_round}\n"\
               f"{self.match_list}\n"
