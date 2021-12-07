from utils.solution import Solution

def part1(input: list[int]) -> int:
    index = len(input) // 2
    average = round(input[index] if index % 2 else sum(input[index - 1 : index + 1]) / 2)
    return sum([abs(p - average) for p in input])

def part2(input: list[int]) -> int:
    average = int(sum(input) / len(input))
    return sum([sum(range(abs(p - average) + 1)) for p in input])

if __name__ == "__main__":
    solution = Solution(7, part1, part2, 'day07.txt')
    solution.input = sorted([int(x) for x in solution.input[0].split(',')])
    solution.run()
