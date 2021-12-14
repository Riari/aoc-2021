from utils.solution import Solution

def solve(input: list[str], days: int) -> int:
    timers = [int(t) for t in input[0].split(',')]
    state = [timers.count(x) for x in range(9)]
    for _ in range(days):
        state.append(state.pop(0))
        state[6] += state[8]

    return sum(state)

solution = Solution(6, lambda input: solve(input, 80), lambda input: solve(input, 256), (5934, 26984457539))
solution.run()
