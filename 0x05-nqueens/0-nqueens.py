#!/usr/bin/env python3

"""Solves the N-Queens problem."""

def n_queens(N: int):
    """Returns all possible solutions for N queens in an NxN board."""
    columns = set()
    positive_diag = set()
    negative_diag = set()
    result = []

    def backtrack(row: int, queens: list):
        """Backtracking algorithm to find possible solutions."""
        if row == N:
            result.append(queens.copy())
            return
        for col in range(N):
            # If placing a queen at (row, col) violates any constraints
            if (
                col in columns
                or (row - col) in negative_diag
                or (row + col) in positive_diag
            ):
                continue
            # If placing a queen at (row, col) is valid:
            columns.add(col)
            negative_diag.add(row - col)
            positive_diag.add(row + col)
            queens.append([row, col])
            backtrack(row + 1, queens)
            # Undoing the changes for the next iteration
            columns.remove(col)
            negative_diag.remove(row - col)
            positive_diag.remove(row + col)
            queens.pop()

    backtrack(0, [])
    return result


def main():
    """Main function."""
    arguments = input("Enter N: ")
    if not arguments.isdigit():
        print("N must be a number")
        exit(1)

    N = int(arguments)
    if N < 4:
        print("N must be at least 4")
        exit(1)

    solutions = n_queens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()

