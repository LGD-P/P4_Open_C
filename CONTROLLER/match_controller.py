
from MODEL.match_model import Match


class MatchController:

    def add_unique_match_list(self, match_list, player_score):
        instance = Match([])
        for match in match_list:
            for joueur in match:
                """
                tuple = ([f"{joueur[0].last_name} {joueur[0].first_name}", f"{player_score[joueur[0]]}"],
                         [f"{joueur[1].last_name} {joueur[1].first_name}", f"{player_score[joueur[1]]}"])
                """
                tuple = ([joueur[0], f"{player_score[joueur[0]]}"],
                         [joueur[1], f"{player_score[joueur[1]]}"])
                instance.match.append(tuple)

        return instance
