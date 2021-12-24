from collections import defaultdict
from utils.vector import Vector3
from utils.solution import Solution

class Step:
    x: range
    y: range
    z: range
    state: bool

    def __init__(self, x: range, y: range, z: range, state: bool):
        self.x = x
        self.y = y
        self.z = z
        self.state = state

def part1(steps: list[Step]) -> int:
    reactor = set()
    region = range(-50, 51)
    for step in steps:
        for x in step.x:
            if x not in region: continue
            for y in step.y:
                if y not in region: continue
                for z in step.z:
                    if z not in region: continue
                    vector = Vector3(x, y, z)
                    if step.state:
                        reactor.add(vector)
                    elif vector in reactor:
                        reactor.remove(vector)
    
    return len(reactor)

def part2(steps: list[Step]) -> int:
    reactor = set()
    region = range(-50, 51)
    for step in steps:
        for x in step.x:
            for y in step.y:
                for z in step.z:
                    vector = Vector3(x, y, z)
                    if step.state:
                        reactor.add(vector)
                    elif vector in reactor:
                        reactor.remove(vector)
    
    return len(reactor)

def process_input(input: list[str]) -> list[Step]:
    steps = []
    for line in input:
        state, cuboid = line.split(' ')
        coords = []
        for coord in cuboid.split(','):
            coord = coord.split('=')[1]
            min, max = coord.split('..')
            min, max = int(min), int(max)
            coords.append(range(min, max + 1))
        
        steps.append(Step(coords[0], coords[1], coords[2], 1 if state == 'on' else 0))
    
    return steps

solution = Solution(22, part1, part2, (590784, 0))
solution.process_input(process_input)
solution.run()
