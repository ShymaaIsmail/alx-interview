#!/usr/bin/python3
"""N Queen Puzzle"""
import sys


def is_safe(board, row, col, n):
    """is_safe for placing the queen to avoid conflict"""
    for i in range(row):
        if (board[i] == col
                or board[i] - i == col - row
                or board[i] + i == col + row):
            return False
    return True


def solve_n_queens(board, row, n):
    """get all n queens solutions"""
    # Base case: If all queens are placed, print the solution
    if row == n:
        print([[i, board[i]] for i in range(n)])
        return

    # Try placing queen in each column of the current row
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(board, row + 1, n)
            board[row] = -1


def n_queens(n):
    """Initialize the board"""
    board = [-1] * n
    solve_n_queens(board, 0, n)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)
if n < 4:
    print("N must be at least 4")
    exit(1)
n_queens(n)
