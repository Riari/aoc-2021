from utils.solution import Solution

def solve(input: list[str], return_first_win: bool) -> int:
    board_index = -1
    numbers = []
    boards = []
    row_width = 5
    for i in range(len(input)):
        line = input[i]
        if i == 0:
            numbers = [int(i) for i in line.split(',')]
        elif line == '':
            board_index += 1
            boards.append([])
        else:
            boards[board_index].extend([int(i) for i in line.split()])

    marked_numbers = [set() for _ in range(len(boards))]
    unmarked_numbers = []
    winning_boards = set()
    last_winning_number: int = None
    for a in range(len(numbers)):
        number = numbers[a]
        for i in range(len(boards)):
            if i in winning_boards:
                continue

            board = boards[i]
            for j in range(len(board)):
                board_number = board[j]
                if board_number != number:
                    continue

                marked_numbers[i].add(board_number)
                
                y = j // row_width
                x = j % row_width
                row = {board[n] for n in range(y * row_width, y * row_width + row_width)}
                column = {board[n] for n in [x] + [row_width * k + x for k in range(1, 5)]}
                
                if row.issubset(marked_numbers[i]) or column.issubset(marked_numbers[i]):
                    board_set = set(board)
                    unmarked_numbers = list(board_set.symmetric_difference(marked_numbers[i]))
                    if return_first_win:
                        return sum(unmarked_numbers) * number

                    winning_boards.add(i)
                    last_winning_number = number
    else:
        return sum(unmarked_numbers) * last_winning_number

solution = Solution(4, lambda input: solve(input, True), lambda input: solve(input, False), (4512, 1924))
solution.run()
