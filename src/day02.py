from utils.solution import Solution

def parse_instruction(instruction: str) -> tuple:
    (direction, units) = instruction.split()
    return (direction, int(units))

def part1(input: list[str]) -> int:
    x, y = 0, 0
    for instruction in input:
        (direction, units) = parse_instruction(instruction)
        match direction:
            case 'forward':
                x += units
            case 'up':
                y -= units
            case 'down':
                y += units

    return x * y

def part2(input: list[str]) -> int:
    x, y, aim = 0, 0, 0
    for instruction in input:
        (direction, units) = parse_instruction(instruction)
        match direction:
            case 'forward':
                x += units
                y += aim * units
            case 'up':
                aim -= units
            case 'down':
                aim += units

    return x * y

if __name__ == "__main__":
    solution = Solution(2, part1, part2, 'day02.txt', str)
    solution.run()
