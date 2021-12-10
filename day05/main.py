from collections import Counter
from utils.solution import Solution

def solve(input: list[str], include_diagonals: bool) -> int:
    counter = Counter()
    for line in input:
        a, b = line.split(' -> ')
        x1, y1 = (int(n) for n in a.split(','))
        x2, y2 = (int(n) for n in b.split(','))

        if x1 == x2:
            counter.update([(x1, y) for y in range(min(y1, y2), max(y1, y2) + 1)])
        elif y1 == y2:
            counter.update([(x, y1) for x in range(min(x1, x2), max(x1, x2) + 1)])
        elif include_diagonals:
            counter.update([
                (x, y) for x, y in zip(
                    range(x1, x2 + 1) if x1 < x2 else range(x1, x2 - 1, -1),
                    range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 1, -1)
                )
            ])

    return sum(c > 1 for c in counter.values())

def part1(input: list[str]) -> int:
    return solve(input, False)

def part2(input: list[str]) -> int:
    return solve(input, True)

if __name__ == "__main__":
    solution = Solution(5, part1, part2, (5, 12))
    solution.run()
