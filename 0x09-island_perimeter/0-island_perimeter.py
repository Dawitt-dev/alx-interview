#!/usr/bin/python3
""" a function that returns the perimeter of
    the island described in grid
"""


def island_perimeter(grid):
    """calculates the perimeter of an island
        represented in a 2D grid
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check top neighbor
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check bottom neighbor
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check left neighbor
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check right neighbor
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
