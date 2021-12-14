from utils.solution import Solution

def part1(input: list[int]) -> int:
    count = 0
    for a, b in zip(input, input[1:]):
        if a < b:
            count += 1

    return count

def part2(input: list[int]) -> int:
    a, b = 0, 0
    count = 0
    window_size = 3
    for i in range(len(input) - window_size + 1):
        b = sum(input[i: i + window_size])
        if a > 0 and b > a:
            count += 1

        a = b

    return count

solution = Solution(1, part1, part2, (7, 5), int)
solution.run()
