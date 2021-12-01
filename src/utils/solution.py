from typing import Callable
from tabulate import tabulate
from .input import read_input

class Solution:
    day: int
    part1: Callable
    part2: Callable
    input: list[str]

    def __init__(self, day: int, part1: Callable, part2: Callable):
        self.day = day
        self.part1 = part1
        self.part2 = part2

    def load_input(self, filename: str):
        self.input = read_input(filename)

    def output(self):
        print(f'## Day {self.day}')
        headers = ['Part One', 'Part Two']
        row = [[self.part1(self.input), self.part2(self.input)]]
        print(tabulate(row, headers, tablefmt='github'))
