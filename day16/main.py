from functools import reduce
from utils.solution import Solution

class Packet:
    version: int
    type_id: int
    value: int

    def __init__(self, version: int, type_id: int):
        self.packets = []
        self.version = version
        self.type_id = type_id

class Decoder:
    sequence: list[str]
    pop_count: int
    version_sum: int

    def __init__(self, hex: str):
        self.sequence = []
        for c in hex: self.sequence.extend(bin(int(c, 16))[2:].zfill(4))
        self.pop_count = 0
        self.version_sum = 0

    def get_bits(self, length: int) -> str:
        bits = ''
        for _ in range(length):
            bits += self.sequence.pop(0)
            self.pop_count += 1

        return bits

    def decode_bits(self, length: int) -> int:
        return int(self.get_bits(length), 2)

    def decode(self) -> Packet:
        packet = Packet(self.decode_bits(3), self.decode_bits(3))
        self.version_sum += packet.version

        packet.value = self.decode_literal() if packet.type_id == 4 else self.decode_operator(packet.type_id)
        return packet

    def decode_literal(self):
        last_group = False
        groups = ''
        while not last_group:
            group = self.get_bits(5)
            groups += group[1:]
            if group.startswith('0'): last_group = True

        return int(groups, 2)

    def decode_operator(self, type_id: int):
        length_type_id = self.decode_bits(1)
        values = []
        match length_type_id:
            case 0: # Length
                length = self.decode_bits(15)
                start_at = self.pop_count
                while self.pop_count < start_at + length: values.append(self.decode().value)
            case 1: # Count
                count = self.decode_bits(11)
                for _ in range(count): values.append(self.decode().value)

        v: int = 0
        match type_id:
            case 0: v = sum(values)
            case 1: v = reduce(lambda x, y: x * y, values)
            case 2: v = min(values)
            case 3: v = max(values)
            case 5: v = int(values[0] > values[1])
            case 6: v = int(values[0] < values[1])
            case 7: v = int(values[0] == values[1])

        return v

def part1(input: list[str]) -> int:
    decoder = Decoder(input[0])
    decoder.decode()
    return decoder.version_sum

def part2(input: list[str]) -> int:
    decoder = Decoder(input[0])
    return decoder.decode().value

solution = Solution(16, part1, part2, (6, 2021))
solution.run()
