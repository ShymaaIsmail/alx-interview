#!/usr/bin/python3

""" calculator for island perimeter"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a 2D grid.

    Parameters:
    grid (list of list of int): A 2D list where 0 represents
    water and 1 represents land.
    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0  # Initialize perimeter counter

    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4  # Each land cell adds 4 to the perimeter

                # Check if the upper cell is also land
                # (i > 0 ensures we're not out of bounds)
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1  # Shared edge, reduce perimeter by 1

                # Check if the lower cell is also land
                # (i < len(grid) - 1 ensures we're not out of bounds)
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1  # Shared edge, reduce perimeter by 1

                # Check if the left cell is also land
                # (j > 0 ensures we're not out of bounds)
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1  # Shared edge, reduce perimeter by 1

                # Check if the right cell is also lan
                # (j < len(grid[i]) - 1 ensures we're not out of bounds)
                if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1  # Shared edge, reduce perimeter by 1

    return perimeter  # Return the total perimeter calculated
