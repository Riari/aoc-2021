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
    state: bool

    def __init__(self, x: range, y: range, z: range, state: bool):
        self.x = x
        self.y = y
        self.z = z
        self.state = state
    
    def get_volume(self):
        x = self.x.stop - self.x.start
        y = self.y.stop - self.y.start
        z = self.z.stop - self.z.start

        return x * y * z

    def get_intersection_volume(self, other: Cuboid, exclude: list[Cuboid]) -> int:
        exclude_x = [x for c in exclude for x in c.x]
        exclude_y = [y for c in exclude for y in c.y]
        exclude_z = [z for c in exclude for z in c.z]

        x = sum([1 for i in other.x if i in self.x and i not in exclude_x])
        y = sum([1 for i in other.y if i in self.y and i not in exclude_y])
        z = sum([1 for i in other.z if i in self.z and i not in exclude_z])

        volume = 0
        if x > 0 and y > 0 and z > 0:
            volume = x * y * z

        return volume

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

def solve(steps: list[Step], init_region = range(-10000, 10000)) -> int:
    on = 0
    cuboids = []
    init_region_only = init_region.stop < 10000
    for step in reversed(steps):
        if init_region_only:
            if step.x.start not in init_region or step.x.stop - 1 not in init_region:
                continue
            if step.y.start not in init_region or step.y.stop - 1 not in init_region:
                continue
            if step.z.start not in init_region or step.z.stop - 1 not in init_region:
                continue

        cuboid = Cuboid(step.x, step.y, step.z, step.state)
        if step.state:
            volume = cuboid.get_volume()
            exclude = []
            for c in cuboids:
                intersection = cuboid.get_intersection_volume(c, exclude)
                volume -= intersection
                if not c.state:
                    exclude.append(c)

            on += volume

        cuboids.append(cuboid)

    return on

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
