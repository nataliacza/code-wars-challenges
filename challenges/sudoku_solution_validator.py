""" 4 kyu
https://www.codewars.com/kata/529bf0e9bdf7657179000008/python

Sudoku Background
Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9,
so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the
digits from 1 to 9. (More info at: http://en.wikipedia.org/wiki/Sudoku)

Sudoku Solution Validator
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board,
and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's,
which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
"""

# Main solution
def valid_solution(board) -> bool:
    check_all = check_all_elements(board)
    single_block = check_single_block(board)

    if not single_block or not check_all:
        return False

    return True


def check_single_block(board) -> bool:
    """ Single block is 3x3. Checking here only first one. """
    fst = sum(board[0][0:3])
    snd = sum(board[1][0:3])
    trd = sum(board[2][0:3])

    total = sum([fst, snd, trd])
    if total != 45:
        return False
    return True

def check_all_elements(board) -> bool:
    """ While iteration over each row, validate also if row has 9 elements, sum of it equals to 45 and
    if there is any zeros - to exclude parts that we're certain are not valid. """
    sum_col = 0
    flag = 0
    while flag < 9:
        for arr in board:
            if len(set(arr)) != 9 or sum(arr) != 45 or arr.count(0) > 0:
                return False
            sum_col += arr[flag]
        if sum_col != 45:
            return False
        sum_col = 0
        flag += 1

    return True


board = [[1, 2, 3, 4, 5, 6, 7, 8, 9],
         [2, 3, 4, 5, 6, 7, 8, 9, 1],
         [3, 4, 5, 6, 7, 8, 9, 1, 2],
         [4, 5, 6, 7, 8, 9, 1, 2, 3],
         [5, 6, 7, 8, 9, 1, 2, 3, 4],
         [6, 7, 8, 9, 1, 2, 3, 4, 5],
         [7, 8, 9, 1, 2, 3, 4, 5, 6],
         [8, 9, 1, 2, 3, 4, 5, 6, 7],
         [9, 1, 2, 3, 4, 5, 6, 7, 8]
         ]

result = valid_solution(board)
print(result)
