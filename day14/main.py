from collections import Counter, defaultdict
from utils.solution import Solution

def solve(input: list[str], steps: int) -> int:
    rules = {}
    for i in range(2, len(input)):
        (a, b), insert = input[i].split(' -> ')
        rules[a, b] = ((a, insert), (insert, b))

    polymer = Counter(zip(input[0], input[0][1:]))

    for _ in range(steps):
        p = defaultdict(int)
        for pair in polymer:
            for insert in rules[pair]:
                p[insert] += polymer[pair]

        polymer = p

    chars = defaultdict(int)
    for pair in polymer:
        chars[pair[0]] += polymer[pair]

    return 1 + max(chars.values()) - min(chars.values())

solution = Solution(14, lambda input: solve(input, 10), lambda input: solve(input, 40), (1588, 2188189693529))
solution.run()
