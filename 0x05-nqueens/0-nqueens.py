#!/usr/bin/python3
"""N queens solution finder module.
"""
import sys


def get_input():
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    return n


def is_attacking(pos0, pos1):
    """Checks if the positions of two queens are in an attacking mode.

    Args:
        pos0 (list or tuple): The first queen's position.
        pos1 (list or tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position else False.
    """
    if pos0[0] == pos1[0] or pos0[1] == pos1[1]:
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])


def build_solution(n, row, positions, solutions):
    """Builds a solution for the n queens problem.

    Args:
        n (int): The size of the chessboard.
        row (int): The current row in the chessboard.
        positions (list of lists of integers): The positions of placed queens.
        solutions (list of lists): The list of possible solutions.
    """
    if row == n:
        solutions.append(positions.copy())
        return
    for col in range(n):
        valid = True
        for pos in positions:
            if is_attacking(pos, [row, col]):
                valid = False
                break
        if valid:
            positions.append([row, col])
            build_solution(n, row + 1, positions, solutions)
            positions.pop()


def print_solutions(solutions):
    """Prints the solutions in the required format.

    Args:
        solutions (list of lists): The list of possible solutions.
    """
    for solution in solutions:
        print(solution)


def main():
    n = get_input()
    solutions = []
    build_solution(n, 0, [], solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
