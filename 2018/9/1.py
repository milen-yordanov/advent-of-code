# See: https://adventofcode.com/2018/day/9#part1

import re
import pprint

input_file_name = 'input.txt'

with open(input_file_name) as f:
    content = f.readlines()

def parse_marbel_game_description(coordinate_str):
    toks = coordinate_str.split(' ')
    return (int(toks[0]), (int(toks[6])))

marble_games = [parse_marbel_game_description(x.strip()) for x in content]

def play_marbles_game(players, last_marble_number):
    players_score = {}
    current_player = 1
    marbles_circle = [0]
    current_marble = 0
    for i in range(1, last_marble_number + 1):
        if (i % 23) == 0:
            if not (current_player in players_score):
                players_score[current_player] = 0

            players_score[current_player] += i

            current_marble -= 7
            current_marble += len(marbles_circle)
            current_marble %= len(marbles_circle)

            players_score[current_player] += marbles_circle[current_marble]
            marbles_circle = marbles_circle[0:current_marble] + marbles_circle[current_marble + 1:]
        else:
            current_marble += 2
            current_marble %= len(marbles_circle)
            if current_marble == 0:
                current_marble = len(marbles_circle)

            marbles_circle = marbles_circle[0:current_marble] + [i,] + marbles_circle[current_marble:]

        current_player += 1
        if current_player > players:
            current_player = 1

    return (players_score, marbles_circle, current_marble, current_player)

def get_highest_score(players_score):
    return max(players_score.values())

for game in marble_games:
    game_result = play_marbles_game(game[0], game[1])
    print (get_highest_score(game_result[0]))