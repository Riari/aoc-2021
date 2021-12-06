from utils.solution import Solution

def solve(input: list[str], days: int) -> int:
    timers = [int(t) for t in input[0].split(',')]
    state = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for t in timers:
        state[t] += 1

    for _ in range(0, days):
        for t in state:
            count = state[t]
            if t == 0:
                state[t] = 0
                state[7] += count
                state[9] += count
            else:
                state[t] = 0
                state[t - 1] += count

    return sum(state.values())

def part1(input: list[str]) -> int:
    return solve(input, 80)

def part2(input: list[str]) -> int:
    return solve(input, 256)

if __name__ == "__main__":
    solution = Solution(6, part1, part2, 'day06.txt')
    solution.run()
