from __future__ import annotations

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
        return f'({self.x},{self.y})'

    def __repr__(self) -> str:
        return self.__str__()

class Vector3:
    x: int
    y: int
    z: int

    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self) -> str:
        return f'({self.x}, {self.y}, {self.z})'

    def __repr__(self) -> str:
        return self.__str__()
