from collections import Counter
from utils.solution import Solution

def solve(input: list[str], steps: int) -> int:
    rules = {}
    for i in range(2, len(input)):
        (a, b), insert = input[i].split(' -> ')
        rules[a, b] = ((a, insert), (insert, b))

    polymer = Counter(zip(input[0], input[0][1:]))

    for _ in range(steps):
        p = Counter()
        for pair in polymer:
            if pair in rules:
                for insert in rules[pair]:
                    p[insert] += polymer[pair]

        polymer = p

    chars = Counter()
    for pair in polymer:
        chars[pair[0]] += polymer[pair]

    common = chars.most_common()
    return 1 + common[0][1] - common[-1][1]

def part1(input: list[str]) -> int:
    return solve(input, 10)

def part2(input: list[str]) -> int:
    return solve(input, 40)

if __name__ == "__main__":
    solution = Solution(14, part1, part2, (1588, 2188189693529))
    solution.run()
