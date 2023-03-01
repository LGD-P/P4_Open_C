class MatchController:

    def add_unique_match_list(self, match_list, player_score):
        instance = []

        for joueur in match_list:

            tuple = ([joueur[0], int(player_score[joueur[0]])],
                     [joueur[1], int(player_score[joueur[1]])])

            instance.append(tuple)

        return instance
