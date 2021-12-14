import os, time
from typing import Callable
from tabulate import tabulate

class Part:
    number: int
    function: Callable
    result: int
    time: float

    def __init__(self, number: int, function: Callable):
        self.number = number
        self.function = function

    def test(self, input: list[str], expected: int):
        result = self.function(input)
        assert (result == expected), f'Part {self.number} test failed; expected {expected} and got {result}'

    def execute(self, input: list[str]):
        start = time.time()
        self.result = self.function(input)
        end = time.time()
        self.time = end - start

    def time_formatted(self) -> str:
        return str(round(self.time, 3)) + 's'

class Solution:
    day: int
    part1: Part
    part2: Part
    test_input: list[str]
    test_results: tuple[int]
    personal_input: list[str]

    def __init__(self, day: int, part1: Callable, part2: Callable, test_results: tuple[int], input_type = str):
        self.day = day
        self.part1 = Part(1, part1)
        self.part2 = Part(2, part2)
        self.test_input = self.__read_input('test', input_type)
        self.test_results = test_results
        self.personal_input = self.__read_input('personal', input_type)

    def __read_input(self, input_filename: str, input_type = str) -> list:
        with open(os.path.join(f'day{str(self.day).zfill(2)}', f'{input_filename}.input'), 'r') as f:
            return list(map(input_type, [line.rstrip('\n') for line in f]))

    def process_input(self, callback: Callable):
        self.test_input = callback(self.test_input)
        self.personal_input = callback(self.personal_input)

    def run(self):
        self.part1.test(self.test_input, self.test_results[0])
        self.part2.test(self.test_input, self.test_results[1])

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
