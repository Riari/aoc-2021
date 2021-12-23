from utils.solution import Solution

def pad(image: list[str], pixel: str, padding: int = 2) -> list[str]:
    padded = []
    dark_row = [pixel * (len(image[0]) + padding * 2)]
    for _ in range(padding): padded.extend(dark_row)
    padded.extend([(pixel * padding) + row + (pixel * padding) for row in image])
    for _ in range(padding): padded.extend(dark_row)

    return padded

def trim(image: list[str], trim: int = 1) -> list[str]:
    return [row[trim:len(row) - trim] for row in image[trim:len(image) - trim]]

def enhance(algorithm: str, image: list[str]) -> list[str]:
    output = []
    for y in range(1, len(image) - 1):
        row = ''
        for x in range(1, len(image[0]) - 1):
            group = ''
            for v in [-1, 0, 1]:
                for h in [-1, 0, 1]:
                    group += '0' if image[y + v][x + h] == '.' else '1'

            row += algorithm[int(group, 2)]

        output.append(row)

    return output

def solve(input: list[str], iterations: int) -> int:
    algorithm = input[0]
    image = pad(input[2:], '.')
    i = 0
    while i < iterations:
        padding_pixel = algorithm[0] if not i % 2 else '.'
        image = pad(enhance(algorithm, image), padding_pixel)
        i += 1

    return sum([row.count('#') for row in image])

solution = Solution(20, lambda input: solve(input, 2), lambda input: solve(input, 50), (35, 3351))
solution.run()
