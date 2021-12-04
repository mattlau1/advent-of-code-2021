from collections import defaultdict
# import pprint


def sol(draw_numbers: list, bingo_boards: dict) -> int:
    # # pp = pprint.PrettyPrinter(indent=4)

    winning_draw_number = -1
    winning_sum = 0
    for draw_number in draw_numbers:
        # go through every bingo board and mark each matching draw_number
        # by flipping it.

        for key in bingo_boards:
            bingo_board = bingo_boards[key]
            winner = False
            for i in range(len(bingo_board)):
                for j in range(len(bingo_board)):
                    if bingo_board[i][j] == draw_number:
                        bingo_board[i][j] *= -1
                        if bingo_board[i][j] == 0:
                            bingo_board[i][j] = -999999999999999
                        # print("about to mark " + str(draw_number))
                        # print('marked:')
                        # print(
                        # '\n'.join(['\t'.join([str(cell) for cell in row]) for row in bingo_board]))

                        # after we have marked this number, we should
                        # check the entire row and column to see if this
                        # bingo board is a winner.

                        complete_col = True

                        # print('checking cols:')
                        # check row
                        for k in range(len(bingo_board[i])):
                            col_item = bingo_board[k][j]
                            # print(f"checking col item: {col_item}")
                            if col_item >= 0:
                                complete_col = False
                                break

                        if complete_col == True:
                            # print('')
                            # print('COMPLETE COLUMN')
                            # print('')

                            winner = True
                            break

                        complete_row = True
                        # print('')
                        # print('checking rows:')
                        # check col
                        for k in range(len(bingo_board[i])):
                            row_item = bingo_board[i][k]
                            # print(f"checking row item: {row_item}")
                            if row_item >= 0:
                                complete_row = False
                                break

                        if complete_row == True:
                            # print('')
                            # print('COMPLETE ROW')
                            # print('')
                            winner = True
                            break
                else:
                    continue
                break
            # print('')
            if winner == True:
                # sum all umarked numbers in this board
                # print("Summing winner board")
                sum = 0
                for i in range(len(bingo_board)):
                    for j in range(len(bingo_board)):
                        if bingo_board[i][j] >= 0:
                            sum += bingo_board[i][j]
                winning_draw_number = draw_number
                winning_sum = sum
                print("winning draw number: " + str(winning_draw_number))
                print("winning sum number: " + str(winning_sum))
                print("winning board: ")
                print(
                    '\n'.join(['\t'.join([str(cell) for cell in row]) for row in bingo_board]))
                return winning_draw_number * winning_sum
    return winning_draw_number * winning_sum


if __name__ == "__main__":
    arr = []
    draws = []
    bingo_board_count = 0

    bingo_boards = defaultdict(lambda: list())
    with open("input.txt") as f:
        lines = f.readlines()
        for line_number, line in enumerate(lines):
            if line_number == 0:
                draws = [int(draw_number.strip())
                         for draw_number in line.split(',')]
            else:
                if len(line) == 0 or len(line) == 1:
                    # start bingo board

                    bingo_board_count += 1

                else:
                    bingo_line = [int(bingo_number.strip())
                                  for bingo_number in line.split()]
                    bingo_boards[bingo_board_count].append(bingo_line)

    # print(f'Draws: {draws}')
    # print('')
    # print("Boards:")
    # # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(dict(bingo_boards))
    print(sol(bingo_boards=bingo_boards, draw_numbers=draws))
