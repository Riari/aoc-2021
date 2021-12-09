from utils.solution import Solution

def part1(input: list[str]) -> int:
    result = 0
    for line in input:
        _, outputs = line.split(' | ')
        outputs = outputs.split(' ')
        result += sum([1 if len(s) in [2, 3, 4, 7] else 0 for s in outputs])

    return result

def part2(input: list[str]) -> int:
    total = 0
    for line in input:
        signals, outputs = line.split(' | ')
        signals = [frozenset(s) for s in signals.split(' ')]
        outputs = [frozenset(o) for o in outputs.split(' ')]
        signal_to_digit = {}
        signal_4, signal_7 = None, None
        for signal in (s for s in signals if len(s) not in [5, 6]):
            d: int
            match len(signal):
                case 2: d = 1
                case 3: d, signal_7 = 7, signal
                case 4: d, signal_4 = 4, signal
                case 7: d = 8

            signal_to_digit[signal] = d

        for s in signals:
            if len(s) == 5: signal_to_digit[s] = 3 if signal_7.issubset(s) else 5 if len(s.intersection(signal_4)) == 3 else 2
            if len(s) == 6: signal_to_digit[s] = 9 if signal_4.issubset(s) else 0 if signal_7.issubset(s) else 6

        output = int("".join([str(signal_to_digit[o]) for o in outputs]))
        total += output

    return total

if __name__ == "__main__":
    solution = Solution(8, part1, part2, 'day08.txt')
    solution.run()
