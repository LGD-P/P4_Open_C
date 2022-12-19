from test_controller import *
from rich import print


# On prends la liste des joueurs
# On récupère l'index des joueurs dans la liste ainsi que leur rang
# On créer un dictionnaire avec pour clef le rang des joueurs

players_rank_list= []
player_index = []

for element in PLAYERS_LIST:
    players_rank_list.append(element.rank)
    player_index.append(PLAYERS_LIST.index(element))


dico_player_position = dict(zip(players_rank_list,player_index))


# On classe le dictionnaire par rang
# Pui on en fait une liste contenant rang/index 


sorted_players_dict = sorted(dico_player_position.items())

print(sorted_players_dict)

player_rank_index_list = []
for k,v in sorted_players_dict:
    player_rank_index_list.append([k,v])



# On créer deux listes avec les rangs des joueurs par ordre croissant
# Puis on fusionne chaque moitié de liste avec la moitié correspondante


first_rank_part = player_rank_index_list[0:4]
second_rank_part = player_rank_index_list[4:9]

first_list_of_match = []
for element_1, element_2 in zip(first_rank_part,second_rank_part):
    first_list_of_match.append([element_1, element_2])
    TOURNAMENT_LIST[0].tours.append([element_1, element_2])

    
# Ainsi il n'y a plus qu'a aller chercher l'index du joueur dans la liste
# Correspondante pour faire l'annonce des matchs.




counter = -1
listing_of_match_first_round = []
for element in first_list_of_match:
    counter += 1
    print(f"{(PLAYERS_LIST[first_list_of_match[counter][0][1]].last_name)} joue contre " \
        f"{(PLAYERS_LIST[first_list_of_match[counter][1][1]].last_name)}")

    listing_of_match_first_round.append(
        ([(PLAYERS_LIST[first_list_of_match[counter][0][1]].last_name),
         (PLAYERS_LIST[first_list_of_match[counter][0][1]].rank)],
        [(PLAYERS_LIST[first_list_of_match[counter][1][1]].last_name),
         (PLAYERS_LIST[first_list_of_match[counter][1][1]].rank)]))

for element in listing_of_match_first_round:
    print(tuple(element))
