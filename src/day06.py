from utils.solution import Solution

def solve(input: list[str], days: int) -> int:
    timers = [int(t) for t in input[0].split(',')]
    state = [timers.count(x) for x in range(9)]
    for _ in range(days):
        state.append(state.pop(0))
        state[6] += state[8]

    return sum(state)

def part1(input: list[str]) -> int:
    return solve(input, 80)

def part2(input: list[str]) -> int:
    return solve(input, 256)

if __name__ == "__main__":
    solution = Solution(6, part1, part2, 'day06.txt')
    solution.run()
