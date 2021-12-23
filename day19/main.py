from utils.solution import Solution
from utils.vector import Vector3

class Scanner:
    id: int
    beacons: list[Vector3]
    overlaps_with: list[int]

    def __init__(self, id: int):
        self.id = id
        self.beacons = []
        self.overlaps_with = []

    def __repr__(self) -> str:
        return f'Scanner {self.id}'

def part1(scanners: list[Scanner]) -> int:
    return 0

def part2(scanners: list[Scanner]) -> int:
    return 0

def process_input(input: list[str]) -> list[Scanner]:
    scanners = []
    id = 0
    scanner = Scanner(id)
    for line in input:
        if line.startswith('---'): continue

        if line == '':
            scanners.append(scanner)
            id += 1
            scanner = Scanner(id)
            continue

        x, y, z = line.split(',')
        scanner.beacons.append(Vector3(int(x), int(y), int(z)))

    return scanners

solution = Solution(19, part1, part2, (0, 0))
solution.process_input(process_input)
solution.run()
