from copy import copy
from utils.solution import Solution

def flip(cucumbers: list[str]) -> list[str]:
    new = []
    for x in range(len(cucumbers[0])):
        row = ''
        for y in range(len(cucumbers)):
            row += cucumbers[y][x]

        new.append(row)

    cucumbers = new

def move(cucumbers: list[str], c: str) -> bool:
    moved = False
    for i in range(len(cucumbers)):
        line = cucumbers[i] + cucumbers[i][0]
        replace = line.replace(c + '.', '.' + c)
        line = replace[-1] + replace[1:-1]
        if cucumbers[i] != line:
            cucumbers[i] = line
            moved = True

    return moved

def part1(input: list[str]) -> int:
    cucumbers = copy(input)
    i = 0
    moving = True
    while moving:
        moving = False
        for c in ['>', 'v']:
            if move(cucumbers, c): moving = True
            flip(cucumbers)

        i += 1

    return i

def part2(input: list[str]) -> int:
    return 0

solution = Solution(25, part1, part2, (58, 0))
solution.run()
