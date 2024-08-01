#!/usr/bin/python3
"""N Queen Puzzle"""
import sys


def is_safe(board, row, col, size):
    """is_safe for placing the queen to avoid conflict"""
    for i in range(row):
        if (board[i] == col
                or board[i] - i == col - row
                or board[i] + i == col + row):
            return False
    return True


def solve_n_queens(board, row, size):
    """get all n queens solutions"""
    # Base case: If all queens are placed, print the solution
    if row == size:
        print([[i, board[i]] for i in range(size)])
        return

    # Try placing queen in each column of the current row
    for col in range(size):
        if is_safe(board, row, col, size):
            board[row] = col
            solve_n_queens(board, row + 1, size)
            board[row] = -1


def n_queens(size: int) -> None:
    """Initialize the board"""
    board = [-1] * size
    solve_n_queens(board, 0, size)


if __name__ == "__main__":
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
