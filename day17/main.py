from __future__ import annotations
from utils.solution import Solution

class Vector2:
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, vector: Vector2) -> Vector2:
        self.x += vector.x
        self.y += vector.y
        return self

    def __str__(self) -> str:
        return f'{self.x},{self.y}'

    def __repr__(self) -> str:
        return f'Vector2({self.__str__()})'

def part1(input: list[str]) -> int:
    min_y = int(input[0].split('..')[1].split(', y=')[1])
    return (min_y + 1) * min_y // 2

def part2(input: list[str]) -> int:
    parts = input[0].split('..')
    subparts = parts[1].split(', y=')
    min_x, max_x = int(parts[0].split('=')[1]), int(subparts[0])
    min_y, max_y = int(parts[2]), int(subparts[1])

    velocities = []
    for x in range(max_x + 50):
        for y in range(max_y, abs(max_y)):
            position = Vector2(0, 0)
            initial_velocity = Vector2(x, y)
            velocity = Vector2(x, y)
            i = 0
            while True:
                i += 1
                position += velocity

                if min_x <= position.x <= max_x and max_y <= position.y <= min_y:
                    velocities.append(initial_velocity)
                    break

                if position.x > max_x or position.y < max_y:
                    break

                if velocity.x > 0: velocity.x -= 1
                if velocity.x < 0: velocity.x += 1
                velocity.y -= 1

    return len(velocities)

solution = Solution(17, part1, part2, (45, 112))
solution.run()
