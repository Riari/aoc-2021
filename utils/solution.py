import os, time
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
    expected: tuple[int]
    test_input: list[str]
    personal_input: list[str]

    def __init__(self, day: int, part1: Callable, part2: Callable, expected: tuple[int], input_type = str):
        self.day = day
        self.part1 = SolutionFunction(part1)
        self.part2 = SolutionFunction(part2)
        self.expected = expected
        self.test_input = self.__read_input('test', input_type)
        self.personal_input = self.__read_input('personal', input_type)

    def __read_input(self, input_filename: str, input_type = str) -> list:
        path = f'day{str(self.day).zfill(2)}/'
        with open(os.path.join(path, f'{input_filename}.input'), 'r') as f:
            return list(map(input_type, [line.rstrip('\n') for line in f]))
    
    def process_input(self, callback: Callable):
        self.test_input = callback(self.test_input)
        self.personal_input = callback(self.personal_input)

    def run(self):
        self.part1.execute(self.test_input)
        self.part2.execute(self.test_input)
        assert (self.part1.result == self.expected[0]), "Part 1 test failed"
        assert (self.part2.result == self.expected[1]), "Part 2 test failed"

        print(f'## Day {self.day}')
        headers = ['', 'Part 1', 'Part 2']

        self.part1.execute(self.personal_input)
        self.part2.execute(self.personal_input)

        rows = [
            ['Result', self.part1.result, self.part2.result],
            ['Time', self.part1.time_formatted(), self.part2.time_formatted()]
        ]

        print(tabulate(rows, headers, tablefmt='github'))
        print(f'Total execution time: {str(round(self.part1.time + self.part2.time, 3))}s')
