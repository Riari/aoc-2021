from utils.solution import Solution

def get_lowpoint_coords(heightmap: list[int]) -> list[tuple]:
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
    lowpoints = [input[y][x] for x, y in get_lowpoint_coords(input)]
    return sum(lowpoints) + len(lowpoints)

def part2(input: list[int]) -> int:
    lowpoint_coords = get_lowpoint_coords(input)
    basin_coords = [set(tuple()) for _ in range(len(lowpoint_coords))]
    neighbours = [
        ( 0, -1), # N
        ( 1,  0), # E
        ( 0,  1), # S
        (-1,  0), # W
    ]

    def check_neighbours(i: int, x: int, y: int):
        for h, v in neighbours:
            nx = x + h
            ny = y + v
            if ny < 0 or ny >= len(input): continue
            if nx < 0 or nx >= len(input[ny]): continue
            if input[ny][nx] == 9: continue
            if input[ny][nx] != input[y][x] + 1: continue
            if (nx, ny) in basin_coords[i]: continue

            basin_coords[i].add((nx, ny))
            check_neighbours(i, nx, ny)

    for i in range(len(lowpoint_coords)):
        x, y = lowpoint_coords[i]
        basin_coords[i].add((x, y))
        check_neighbours(i, x, y)

    basin_coords.sort(key = len)
    basin_coords.reverse()

    return len(basin_coords[0]) * len(basin_coords[1]) * len(basin_coords[2])

if __name__ == "__main__":
    solution = Solution(9, part1, part2, 'day09.txt')
    solution.input = [[int(digit) for digit in line] for line in [l for l in solution.input]]
    solution.run()
