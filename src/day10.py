from utils.solution import Solution

def part1(input: list[str]) -> int:
    error_score = 0
    pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    for line in input:
        stack = []
        for c in line:
            if c in pairs.keys():
                stack.append(c)
            elif pairs[stack[-1]] == c:
                stack.pop()
            else:
                match c:
                    case ')': error_score += 3
                    case ']': error_score += 57
                    case '}': error_score += 1197
                    case '>': error_score += 25137
                break

    return error_score

def part2(input: list[str]) -> int:
    return 0

if __name__ == "__main__":
    solution = Solution(10, part1, part2, 'day10.txt')
    solution.run()
