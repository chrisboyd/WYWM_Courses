# Christopher Boyd
# chris@christopherboyd.ca
#
# WYWM Python Programming Fundamentals
# Assignment - Python Summative

def create_board(line_set):
    # Format the board as a 2d array of ints given an array of strings
    # with each index being a row of the board.
    # sample input: "123456789"
    # sample output: [1,2,3,4,5,6,7,8,9]
    # only 1 line show for brevity
    #
    # Restrictions: Expects line_set input to have 9 lines

    board = [[0 for row in range(9)] for col in range(9)]
    row = 0;
    col = 0;
    for r in line_set:
        if r != '' and row < 9:
            for n in r:
                board[row][col] = int(n)
                col += 1
            row += 1
            col = 0
    return board


def print_board(board):
    # Given board, formats and appends the board to 'solved_puzzles.txt'
    # with format as shown:
    # 1 5 3 |6 2 7 |8 4 9
    # 4 2 8 |7 3 5 |1 9 6
    # 3 1 5 |4 7 9 |6 8 2
    # ------+------+------
    # 5 3 1 |2 4 6 |9 7 8
    # 2 6 7 |1 9 8 |3 5 4
    # 9 7 4 |5 8 1 |2 6 3
    # ------+------+------
    # 6 4 9 |8 5 2 |7 3 1
    # 7 8 2 |9 6 3 |4 1 5
    # 8 9 6 |3 1 4 |5 2 7

    with open('solved_puzzles.txt', 'a+') as f:
        for row in range(len(board)):
            if row % 3 == 0 and row != 0:
                f.write("------+------+------\n")

            for col in range(len(board[0])):
                if col % 3 == 0 and col != 0:
                    f.write("|")

                if col == 8:
                    f.write(str(board[row][col]))
                else:
                    f.write(str(board[row][col]) + " ")
            f.write("\n")

        f.write("----------------------------\n")


def print_error():
    # outputs error message that given puzzle could not be solved

    with open('solved_puzzles.txt', 'a+') as f:
        f.write("----------------------------\n")
        f.write("**Puzzle could not be solved**\n")
        f.write("----------------------------\n")


def find_empty(board):
    # Searches board for the first empty square,
    # with empty being defined as a square equal to 0.
    # returns result as row,col

    for row in range(len(board)):
        for col in range(len(board[0])):
            if (board[row][col] == 0):
                return (row, col)
    return None


def valid(board, num, pos):
    # Determines if placing num at pos, defined as [row][col],
    # of board is a valid move, ie num does not already exist
    # in the row, col or square that pos belongs to.
    # returns True or False

    # valid row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # valid column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # valid square
    square_row = pos[1] // 3
    square_col = pos[0] // 3

    for i in range(square_col * 3, square_col * 3):
        for j in range(square_row * 3, square_row * 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(board):
    # Use backtracking to attempt every possible solution
    # until the first successful solution is found, or all are
    # attempted.
    # returns True or False if the board is solved or not

    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    return False


# driver code to run the sudoku puzzle solver
# reads from 'blank_puzzles.txt and writes the
# solution to 'solved_puzzles.txt

with open('blank_puzzles.txt') as f:
    lines = [line.rstrip() for line in f]
    line_set = []
    for r in lines:
        if r != "":
            line_set.append(r)
        else:
            board = create_board(line_set)
            if solve(board):
                print_board(board)
            else:
                print_error(line_set)
            line_set = []
