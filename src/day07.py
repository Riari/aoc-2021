from utils.solution import Solution

def part1(input: list[str]) -> int:
    positions = [int(x) for x in input[0].split(',')]
    size = len(positions)
    index = size // 2
    average = round(sorted(positions)[index] if index % 2 else sum(sorted(positions)[index - 1 : index + 1]) / 2)
    return sum([abs(p - average) for p in positions])

def part2(input: list[str]) -> int:
    positions = [int(x) for x in input[0].split(',')]
    average = int(sum(positions) / len(positions))
    return sum([sum(range(abs(p - average) + 1)) for p in positions])

if __name__ == "__main__":
    solution = Solution(7, part1, part2, 'day07.txt')
    solution.run()
