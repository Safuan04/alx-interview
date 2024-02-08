#!/usr/bin/python3
"""Solving the nqueens Challenge"""
from sys import argv, exit


if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)

try:
    N = int(argv[1])
except ValueError:
    print('N must be a number')
    exit(1)

if N < 4:
    print('N must be at least 4')
    exit(1)


def n_queens(N: int):
    """returns all possible solutions for N queens in NxN board"""
    columns = set()
    positiveDiag = set()
    negativeDiag = set()
    result = []

    def backtrack(row: int, queens: list):
        """backtracking algorithm to find possible solutions"""
        if row == N:
            result.append(queens.copy())
            return
        for col in range(N):
            # if placing a queen at (row, col) violates any constraints
            if (col in columns
                    or (row - col) in negativeDiag
                    or (row + col) in positiveDiag):
                continue
            # If placing a queen at (row, col) is valid:
            columns.add(col)
            negativeDiag.add(row - col)
            positiveDiag.add(row + col)
            queens.append([row, col])
            backtrack(row + 1, queens)
            # Undoing the changes for the next iteration
            columns.remove(col)
            negativeDiag.remove(row - col)
            positiveDiag.remove(row + col)
            queens.pop()
    backtrack(0, [])
    return result


if __name__ == "__main__":
    solutions = n_queens(N)
    for solution in solutions:
        print(solution)
