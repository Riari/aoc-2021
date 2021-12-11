from typing import Callable
from utils.solution import Solution

def solve(input: list[list[int]], end_step: Callable) -> int:
    height, width = range(len(input)), range(len(input[0]))
    coordinates = [(y, x) for y in height for x in width]

    def flash(y: int, x: int) -> int:
        flashes = 1
        input[y][x] = -1
        for v in [-1, 0, 1]:
            for h in [-1, 0, 1]:
                ny, nx = y + v, x + h

                if ny not in height or nx not in width or input[ny][nx] == -1:
                    continue

                input[ny][nx] += 1
                if input[ny][nx] > 9:
                    flashes += flash(ny, nx)

        return flashes

    step, flashes = 0, 0
    while True:
        step += 1
        step_flashes = 0

        for y, x in coordinates: input[y][x] += 1

        for y, x in coordinates:
            if input[y][x] == 10:
                neighbour_flashes = flash(y, x)
                step_flashes += neighbour_flashes
                flashes += neighbour_flashes

        for y, x in coordinates:
            if input[y][x] == -1:
                input[y][x] = 0

        result = end_step(step, flashes, step_flashes)
        if result > 0: return result

def part1(input: list[list[int]]) -> int:
    return solve(input, lambda step, flashes, step_flashes: flashes if step == 100 else 0)

def part2(input: list[list[int]]) -> int:
    return solve(input, lambda step, flashes, step_flashes: 100 + step if step_flashes == len(input) * len(input[0]) else 0)

if __name__ == "__main__":
    solution = Solution(11, part1, part2, (1656, 195))
    solution.process_input(lambda input: [list(map(int, l)) for l in input])
    solution.run()
