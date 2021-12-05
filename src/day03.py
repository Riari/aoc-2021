from typing import Callable
from utils.solution import Solution

def part1(input: list[str]) -> int:
    rotated = list(zip(*input[::-1]))
    width = len(rotated[0])
    height = len(rotated)
    gamma = ['0'] * height
    epsilon = ['0'] * height

    for i in range(height):
        bits = rotated[i]
        if bits.count('1') > (width / 2):
            gamma[i] = '1'
            epsilon[i] = '0'
        else:
            gamma[i] = '0'
            epsilon[i] = '1'

    gamma = int(''.join(gamma), 2)
    epsilon = int(''.join(epsilon), 2)
    return gamma * epsilon

def part2(input: list[str]) -> int:
    rotated = list(zip(*input[::-1]))
    width = len(rotated[0])
    height = len(rotated)
    oxygen_indices = range(width)
    co2_indices = range(width)

    def filter_rating(bits: tuple, indices: list[int], get_match_bit: Callable) -> list[int]:
        match_bit = get_match_bit([c for j, c in enumerate(bits) if j in indices])
        return [j for j in indices if input[j][i] == match_bit]

    for i in range(height):
        if len(oxygen_indices) > 1:
            oxygen_indices = filter_rating(reversed(rotated[i]), oxygen_indices,
                lambda filtered_bits: '1' if filtered_bits.count('1') >= (len(filtered_bits) / 2) else '0')
        if len(co2_indices) > 1:
            co2_indices = filter_rating(reversed(rotated[i]), co2_indices, 
                lambda filtered_bits: '0' if filtered_bits.count('0') <= (len(filtered_bits) / 2) else '1')

    oxygen_generator_rating = int(input[oxygen_indices[0]], 2)
    co2_scrubber_rating = int(input[co2_indices[0]], 2)

    return oxygen_generator_rating * co2_scrubber_rating

if __name__ == "__main__":
    solution = Solution(3, part1, part2, 'day03.txt')
    solution.run()
