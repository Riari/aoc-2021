import time
from typing import Callable
from tabulate import tabulate

class SolutionFunction:
    function: Callable
    result: int
    time: float

    def __init__(self, function: Callable):
        self.function = function

    def execute(self, input: list[str]):
        start = time.time()
        self.result = self.function(input)
        end = time.time()
        self.time = end - start

    def time_formatted(self) -> str:
        return str(round(self.time, 3)) + 's'

class Solution:
    day: int
    part1: SolutionFunction
    part2: SolutionFunction
    input: list[str]

    def __init__(self, day: int, part1: Callable, part2: Callable, input_filename: str, input_type = str):
        self.day = day
        self.part1 = SolutionFunction(part1)
        self.part2 = SolutionFunction(part2)
        self.input = self.__read_input(input_filename, input_type)

    def __read_input(self, input_filename: str, input_type = str) -> list:
        with open(f'input/{input_filename}', 'r') as f:
            return list(map(input_type, f))

    def run(self):
        print(f'## Day {self.day}')
        headers = ['', 'Part 1', 'Part 2']

        self.part1.execute(self.input)
        self.part2.execute(self.input)

        rows = [
            ['Result', self.part1.result, self.part2.result],
            ['Time', self.part1.time_formatted(), self.part2.time_formatted()]
        ]

        print(tabulate(rows, headers, tablefmt='github'))
        print(f'Total execution time: {str(round(self.part1.time + self.part2.time, 3))}s')
