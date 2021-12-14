from utils.solution import Solution

def get_lowpoints(heightmap: list[int]) -> list[tuple]:
    coords = []
    for y in range(len(heightmap)):
        row = heightmap[y]
        for x in range(len(row)):
            h = row[x]
            if x > 0 and row[x - 1] <= h: continue
            if x < len(row) - 1 and row[x + 1] <= h: continue
            if y > 0 and heightmap[y - 1][x] <= h: continue
            if y < len(heightmap) - 1 and heightmap[y + 1][x] <= h: continue
            coords.append((x, y))

    return coords

def part1(input: list[int]) -> int:
    return sum([input[y][x] + 1 for x, y in get_lowpoints(input)])

def part2(input: list[int]) -> int:
    lowpoints = get_lowpoints(input)
    basins = [set(tuple()) for _ in range(len(lowpoints))]
    neighbours = [
        ( 0, -1), # N
        ( 1,  0), # E
        ( 0,  1), # S
        (-1,  0), # W
    ]
    rows, cols = range(len(input)), range(len(input[0]))

    def check_neighbours(i: int, x: int, y: int) -> None:
        for h, v in neighbours:
            nx, ny = x + h, y + v
            if ny not in rows or nx not in cols: continue
            if input[ny][nx] == 9: continue
            if (nx, ny) in basins[i]: continue

            basins[i].add((nx, ny))
            check_neighbours(i, nx, ny)

    for i in range(len(lowpoints)):
        x, y = lowpoints[i]
        basins[i].add((x, y))
        check_neighbours(i, x, y)

    basins.sort(key = len)
    basins.reverse()

    return len(basins[0]) * len(basins[1]) * len(basins[2])

solution = Solution(9, part1, part2, (15, 1134))
solution.process_input(lambda input: [[int(digit) for digit in line] for line in input])
solution.run()
