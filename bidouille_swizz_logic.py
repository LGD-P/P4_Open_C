from test_controller import *



players_list_by_rank = []
player_index = []

for element in PLAYERS_LIST:
    players_list_by_rank.append(element.rank)
    player_index.append(PLAYERS_LIST.index(element))


print("")
print("Position des joueur et classement")

dico_player_position = dict(zip(players_list_by_rank,player_index))



print(dico_player_position)
print("")





print("DICTIONNAIRE CLASSE")
print("")



sd = sorted(dico_player_position.items())
test = []
for k,v in sd:
    test.append([k,v])

print(test)




print("")
print("LISTE DES RANGS")
print("")
print(players_list_by_rank)
print("")
print("LISTE DES INDEX")
print("")
players_list_by_rank = sorted(players_list_by_rank)
print(player_index)
print("")
print("LISTE COUPEE EN DEUX TRIEE PAR RANG")
print("")
print(players_list_by_rank[0:4])
print(players_list_by_rank[4:9])
print("")

premiere_partie = players_list_by_rank[0:4]
seconde_partie = players_list_by_rank[4:9]



pair = []

for element_1,element_2 in zip(premiere_partie,seconde_partie):
    pair.append([element_1,element_2])
    
print(pair)


pp = test[0:4]

sp = test[4:9]


test3 = []
for el1, el2 in zip(pp,sp):
    test3.append([el1,el2])
    
print("*"*10)
for element in test3:
    print(element)


print(test3[0][0][1])

print(PLAYERS_LIST[test3[0][0][1]].last_name)