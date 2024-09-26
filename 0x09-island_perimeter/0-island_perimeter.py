#!/usr/bin/python3
'''module: 5-island_perimeter
 returns the perimeter of the island based on `grid`
 grid is a list of list of integers:
    0 represents a water zone
    1 represents a land zone
    One cell is a square with side length 1
    Grid cells are connected horizontally/vertically (not diagonally).
    Grid is rectangular, width and height don’t exceed 100
Grid is completely surrounded by water, and there is one island (or nothing).
The island doesn’t have “lakes”
    (water inside that isn’t connected to the water around the island).
'''


def island_perimeter(grid):
    '''
    computes the perimeter of the island described in the grid.

    args:
        grid: list of list of integers representing the island.

    returns:
        the perimeter of the island.

    '''
    perimeter = 0

    # check for cell in grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                # check if the cell has water on any of its four sides
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                if i == len(grid) - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter


if __name__ == '__main__':
    print(island_perimeter(grid))
