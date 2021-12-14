from utils.solution import Solution

def fold(input: list[str], stop_on_first: bool) -> list[list[str]]:
    coords = []
    folds = []
    for line in input:
        if line == '': continue
        if line.startswith('fold'):
            fold = line.split('=')
            folds.append((fold[0][11], int(fold[1])))
        else:
            x, y = map(int, line.split(','))
            coords.append((x, y))

    width = max(c[0] for c in coords)
    height = max(c[1] for c in coords)
    grid = [['.' for _ in range(width + 1)] for _ in range(height + 1)]

    for x, y in coords:
        grid[y][x] = '#'

    for i in range(len(folds)):
        axis, at = folds[i]
        if axis == 'y':
            for row in range(1, at + 1):
                for x in range(len(grid[0])):
                    if grid[at + row][x] != '.':
                        grid[at - row][x] = '#'
            for _ in range(at + 1):
                grid.pop()

        if axis == 'x':
            for y in range(len(grid)):
                for col in range(1, at + 1):
                    if grid[y][at + col] != '.':
                        grid[y][at - col] = '#'
                for _ in range(at + 1):
                    grid[y].pop()

        if stop_on_first and i == 0:
            break

    return grid

def part1(input: list[str]) -> int:
    grid = fold(input, True)
    return sum(row.count('#') for row in grid)

def part2(input: list[str]) -> int:
    grid = fold(input, False)
    for row in grid:
        for c in row:
            print('#  ' if c == '#' else '   ', end='')
        print('\n')
    return 0

solution = Solution(13, part1, part2, (17, 0))
solution.run()
