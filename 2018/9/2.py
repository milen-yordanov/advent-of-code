# See: https://adventofcode.com/2018/day/9#part2

import re
import pprint

input_file_name = 'input.txt'

with open(input_file_name) as f:
    content = f.readlines()

def parse_marbel_game_description(coordinate_str):
    toks = coordinate_str.split(' ')
    return (int(toks[0]), (int(toks[6])))

marble_games = [parse_marbel_game_description(x.strip()) for x in content]


class Node(object):
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next

class MarbleCircle(object):
    current = None
    def __init__(self):
        node = Node(0, None, None)
        node.next = node
        node.prev = node
        self.current = node

    def remove(self):
        old_current = self.current
        self.current = self.current.next
        self.current.prev = old_current.prev
        old_current.prev.next = self.current

    def append(self, data):
        node = Node(data, self.current, self.current.next)
        self.current.next.prev = node
        self.current.next = node
        self.current = node

    def move_forward(self, steps):
        for _ in range(steps):
            self.current = self.current.next

    def move_backward(self, steps):
        for _ in range(steps):
            self.current = self.current.prev


def play_marbles_game(players, last_marble_number):
    players_score = {}
    current_player = 1
    marbles_circle = MarbleCircle()
    for i in range(1, last_marble_number + 1):
        if (i % 23) == 0:
            if not (current_player in players_score):
                players_score[current_player] = 0

            players_score[current_player] += i
            marbles_circle.move_backward(7)
            players_score[current_player] += marbles_circle.current.data
            marbles_circle.remove()
        else:
            marbles_circle.move_forward(1)
            marbles_circle.append(i)

        current_player += 1
        if current_player > players:
            current_player = 1

    return (players_score, marbles_circle, current_player)

def get_highest_score(players_score):
    return max(players_score.values())

for game in marble_games:
    game_result = play_marbles_game(game[0], game[1] * 100)
    print (get_highest_score(game_result[0]))
