

class Round:
    def __init__(self, match_list, name,
                 starting_hour, ending_hour,
                 number_of_round, tournament_name):

        self.match_list = match_list
        self.name = name
        self.starting_hour = starting_hour
        self.ending_hour = ending_hour
        self.number_of_round = number_of_round
        self.tournament_name = tournament_name

    def __str__(self):

        if self.ending_hour == None:
            return f"- {self.name}\n"\
                f"- Début de round : "\
                f"{self.starting_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n"\
                f"- Fin de round : pas encore d'heure de fin"\
                f"- Liste des match: {self.match_list}\n"
        else:
            return f"- {self.name}\n"\
                f"- Début de round : "\
                f"{self.starting_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n"\
                f"- Fin de round : "\
                f"{self.ending_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n"\
                f"- Liste des match: {self.match_list}\n"

    def __repr__(self):
        if self.ending_hour == None:
            return f"{self.tournament_name}\n"\
                f"{self.name}\n"\
                f"{self.starting_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n"\
                f"Pas encore d'heure de fin\n"\
                f"{self.number_of_round}\n"\
                f"{self.match_list}\n"

        else:
            return f"{self.tournament_name}\n"\
                f"{self.name}\n"\
                f"{self.starting_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n"\
                f"{self.ending_hour.strftime('%d-%m-%Y - %H:%M:%S')}\n"\
                f"{self.number_of_round}\n"\
                f"{self.match_list}\n"

    """
    return {
        "tournament_name": self.tournament_name,
        "name": self.name,
        "starting_hour": self.starting_hour,
        "ending_hour": self.ending_hour,
        "number_of_rounf": self.number_of_round,
        "match_list": match_list_serialized
    }
    """
