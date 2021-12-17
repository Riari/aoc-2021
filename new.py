#!/usr/bin/env python3
import os, sys

day = sys.argv[1] if len(sys.argv) > 1 else input("Enter day: ")
dir = 'day' + day.zfill(2)
path = os.path.join(os.getcwd(), dir)

if os.path.exists(os.path.join(path, 'main.py')):
    exit(f'{dir} already exists')

if not os.path.exists(path):
    os.mkdir(path)

f = open(os.path.join(path, 'main.py'), 'w')
f.write('''from utils.solution import Solution

def part1(input: list[str]) -> int:
    return 0

def part2(input: list[str]) -> int:
    return 0

solution = Solution({day}, part1, part2, (0, 0))
solution.run()
'''.format(day=day))
f.close()

for file in ['personal.input', 'readme.md', 'test.input']:
    open(os.path.join(path, file), 'w').close()

exit(f'{dir} created')
