from utils.solution import Solution

def solve(input: list[str], return_error_score: bool, scores: dict) -> int:
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    results = []
    for line in input:
        stack = []
        for c in line:
            if c in pairs:
                stack.append(pairs[c])
            elif stack[-1] == c:
                stack.pop()
            else:
                if return_error_score:
                    results.append(scores[c])
                break
        else:
            if return_error_score: continue
            score = 0
            for c in stack[::-1]:
                score *= 5
                score += scores[c]
            results.append(score)

    results.sort()
    return sum(results) if return_error_score else results[len(results) // 2]

def part1(input: list[str]) -> int:
    return solve(input, True, {')': 3, ']': 57, '}': 1197, '>': 25137})

def part2(input: list[str]) -> int:
    return solve(input, False, {')': 1, ']': 2, '}': 3, '>': 4})

solution = Solution(10, part1, part2, (26397, 288957))
solution.run()
