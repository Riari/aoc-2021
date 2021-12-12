from collections import defaultdict, Counter
from utils.solution import Solution

def count_paths(graph: dict[list[str]], revisit_small: bool, node: str = 'start', visited: list = list()) -> list:
    if node == 'end': return 1

    c = 0
    for n in graph[node]:
        v = visited + [node]
        if n.isupper() or n not in v or revisit_small and max(Counter(filter(str.islower, v)).values()) == 1:
            c += count_paths(graph, revisit_small, n, v)

    return c

def part1(input: dict[list[str]]) -> int:
    return count_paths(input, False)

def part2(input: list[str]) -> int:
    return count_paths(input, True)

def build_graph(input: list[str]) -> dict[list[str]]:
    graph = defaultdict(list)
    for line in input:
        l, r = line.split('-')
        if l != 'end' and r != 'start': graph[l].append(r)
        if r != 'end' and l != 'start': graph[r].append(l)

    return graph

if __name__ == "__main__":
    solution = Solution(12, part1, part2, (19, 103))
    solution.process_input(build_graph)
    solution.run()
