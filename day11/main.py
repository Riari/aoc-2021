from utils.solution import Solution

def solve(input: list[list[int]], part_1: bool) -> int:
    height, width = range(len(input)), range(len(input[0]))

    def flash(y: int, x: int) -> int:
        f = 1
        input[y][x] = -1
        for v in [-1, 0, 1]:
            for h in [-1, 0, 1]:
                ny = y + v
                nx = x + h

                if ny not in height or nx not in width or input[ny][nx] == -1:
                    continue

                input[ny][nx] += 1
                if input[ny][nx] > 9:
                    f += flash(ny, nx)

        return f

    step, flashes = 0, 0
    while True:
        step += 1
        step_flashes = 0

        for y in height:
            for x in width:
                input[y][x] += 1

        for y in height:
            for x in width:
                if input[y][x] == 10:
                    neighbour_flashes = flash(y, x)
                    step_flashes += neighbour_flashes
                    flashes += neighbour_flashes

        for y in height:
            for x in width:
                if input[y][x] == -1:
                    input[y][x] = 0

        if part_1 and step == 100:
            return flashes

        if step_flashes == width.stop * height.stop:
            return 100 + step # Part 1 did the first 100 steps

def part1(input: list[list[int]]) -> int:
    return solve(input, True)

def part2(input: list[list[int]]) -> int:
    return solve(input, False)

if __name__ == "__main__":
    solution = Solution(11, part1, part2, (1656, 195))
    solution.process_input(lambda input: [list(map(int, l)) for l in input])
    solution.run()
