from collections import defaultdict
from queue import PriorityQueue
from utils.solution import Solution

def solve(input: list[list[str]], grid_size: int = 1):
    grid = [list(map(int, line)) for line in input]
    width, height = len(grid[0]), len(grid)
    queue = PriorityQueue()
    distances = {}
    visited = defaultdict(bool)

    if grid_size > 1:
        for _ in range((grid_size - 1) * height):
            grid.append([])

    for tile_y in range(grid_size):
        for tile_x in range(grid_size):
            if tile_y == 0 and tile_x == 0: continue
            for y in range(height):
                for x in range(width):
                    cell = grid[y][x]
                    new = cell + tile_y + tile_x
                    if new > 9: new = new - 9
                    grid[tile_y * height + y].append(new)

    width, height = len(grid[0]), len(grid)
    queue.put((0, (0, 0)))

    for x in range(width):
        for y in range(height):
            if x == 0 and y == 0: continue
            distances[(x, y)] = 10000000

    def get_neighbours(point: tuple) -> list:
        neighbours = []
        if point[0] - 1 in range(width): neighbours.append((point[0] - 1, point[1]))
        if point[0] + 1 in range(width): neighbours.append((point[0] + 1, point[1]))
        if point[1] - 1 in range(height): neighbours.append((point[0], point[1] - 1))
        if point[1] + 1 in range(height): neighbours.append((point[0], point[1] + 1))
        return neighbours

    at = (0, 0)
    while at < (width - 1, height - 1):
        priority, at = queue.get()
        neighbours = get_neighbours(at)
        for n in neighbours:
            if visited[n] or n[0] == 0 and n[1] == 0: continue
            p = priority + grid[n[1]][n[0]]
            if distances[n] > p:
                distances[n] = p
                queue.put((distances[n], n))

    return distances[(width - 1, height - 1)]

def part2(input: list[str]) -> int:
    return 0

solution = Solution(15, solve, lambda input: solve(input, 5), (40, 315))
solution.run()
