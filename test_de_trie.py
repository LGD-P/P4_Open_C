
tours = [
    [[1, 2], [7, 4], [3, 6], [5, 8]],
    [[1, 7], [2, 4], [2, 6], [3, 8]]
]


round_3 = [[5, 7], [7, 4], [2, 6], [9, 8]]


for match_1 in round_3:
    for match_list in tours:
        for match in match_list:
            while round_3[-1] == tours[-1][-1]:
                position = round_3.index(match_1)
                player_to_move = round_3[-1][0]
                player_to_replace = round_3[-2][0]
                round_3[-2].append(player_to_move)
                round_3[-1].append(player_to_replace)
                del (round_3[-2][0])
                del (round_3[-1][0])

            else:
                while match == match_1:
                    position = round_3.index(match_1)
                    player_to_move = round_3[position][0]
                    player_to_replace = round_3[position+1][0]
                    round_3[position+1].append(player_to_move)
                    round_3[position].append(player_to_replace)
                    del (round_3[position+1][0])
                    del (round_3[position][0])

print(tours)
