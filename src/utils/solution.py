from typing import Callable
from tabulate import tabulate

class Solution:
    day: int
    part1: Callable
    part2: Callable
    input: list[str]

    def __init__(self, day: int, part1: Callable, part2: Callable, input_filename: str):
        self.day = day
        self.part1 = part1
        self.part2 = part2
        self.input = self.__read_input(input_filename)

    def __read_input(self, input_filename: str) -> list[str]:
        file = open(f'input/{input_filename}', 'r')
        return file.readlines()

    def run(self):
        print(f'## Day {self.day}')
        headers = ['Part One', 'Part Two']
        row = [[self.part1(self.input), self.part2(self.input)]]
        print(tabulate(row, headers, tablefmt='github'))
