from __future__ import annotations
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

class Cuboid:
    x: range
    y: range
    z: range

    def __init__(self, x: range, y: range, z: range):
        self.x = x
        self.y = y
        self.z = z

    def intersects_with(self, other: Cuboid) -> bool:
        has_x = other.x.start in self.x or other.x.stop - 1 in self.x
        if has_x: return True
        has_y = other.y.start in self.y or other.y.stop - 1 in self.y
        if has_y: return True
        return other.z.start in self.z or other.z.stop - 1 in self.z

    def split_by(self, other: Cuboid) -> tuple:
        # TODO: split into multiple cuboids, minus other
        return ()

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

def solve(steps: list[Step], init_region = range(-10000, 10000)) -> int:
    reactor: set[Cuboid] = set()
    init_region_only = init_region.stop < 10000
    for step in steps:
        if init_region_only:
            if step.x.start not in init_region or step.x.stop - 1 not in init_region:
                continue
            if step.y.start not in init_region or step.y.stop - 1 not in init_region:
                continue
            if step.z.start not in init_region or step.z.stop - 1 not in init_region:
                continue

        cuboid = Cuboid(step.x, step.y, step.z)
        for c in reactor:
            # TODO: determine if cuboid intersects c. if it does, dissect c by cuboid, insert the resulting cuboids into the set. if step.state == True, insert cuboid into the set too.
            pass

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

solution = Solution(22, lambda input: solve(input, range(-50, 51)), solve, (590784, 0))
solution.process_input(process_input)
solution.run()
