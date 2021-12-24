import functools
from copy import deepcopy
from collections import defaultdict
from utils.solution import Solution

class Player:
    position: int
    score: int

    def __init__(self, position: int, score: int = 0):
        self.position = position
        self.score = score

    def move(self, spaces: int):
        self.position = (self.position + spaces - 1) % 10 + 1
        self.score += self.position

class DeterministicDie:
    current: int = 0
    roll_count: int = 0

    def roll(self):
        self.current = self.current + 1 if self.current < 100 else 1
        self.roll_count += 1

        return self.current

def part1(input: list[Player]) -> int:
    players = deepcopy(input)
    winning_score = 1000
    die = DeterministicDie()

    end_game = False
    while not end_game:
        for i in range(len(players)):
            player = players[i]
            player.move(die.roll() + die.roll() + die.roll())
            if player.score >= winning_score:
                end_game = True
                losing_player = 0 if i == 1 else 1
                break

    return die.roll_count * players[losing_player].score

# Based on https://github.com/SwampThingTom/AoC2021/blob/main/Python/21-DiracDice/DiracDice.py
dirac_sums = defaultdict(int)
for a in range(1, 4):
    for b in range(1, 4):
        for c in range(1, 4):
            dirac_sums[a + b + c] += 1

@functools.lru_cache(maxsize=None)
def play_dirac(player_a_position: int, player_b_position: int, player_a_score: int, player_b_score: int) -> tuple:
    if player_a_score >= 21:
        return 1, 0
    if player_b_score >= 21:
        return 0, 1

    total_player_a_wins = 0
    total_player_b_wins = 0

    for sum in dirac_sums:
        new_pos = (player_a_position + sum - 1) % 10 + 1
        new_score = player_a_score + new_pos

        player_b_wins, player_a_wins = play_dirac(player_b_position, new_pos, player_b_score, new_score)

        win_count = dirac_sums[sum]
        total_player_a_wins += player_a_wins * win_count
        total_player_b_wins += player_b_wins * win_count

    return total_player_a_wins, total_player_b_wins

def part2(input: list[Player]) -> int:
    players = deepcopy(input)
    wins = play_dirac(players[0].position, players[1].position, players[0].score, players[1].score)

    return max(wins)

solution = Solution(21, part1, part2, (739785, 444356092776315))
solution.process_input(lambda input: [Player(int(line.split(': ')[1])) for line in input])
solution.run()
