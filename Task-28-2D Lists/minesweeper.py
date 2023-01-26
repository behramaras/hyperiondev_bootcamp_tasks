# This program takes a grid of '#' and '-', where each '#' represents a mine and each '-' represents a mine-free spot.
# This program returns a grid, where each dash is replaced by a digit, indicating the number of mines immediately adjacent to the spot.

import numpy as np

grid = [["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]]

# Initialised number_of_rows and number_of_cols.

number_of_rows = len(grid) - 1
number_of_cols = len(grid[number_of_rows]) - 1

# This function prints the latest version of the grid.

def print_grid():
    new_grid = np.array(grid)
    print(new_grid)

# This function takes two parameters and calculates the number of mines according to these parameters.

def count_mines(r_index, c_index):
    numb_mine = 0

    if r_index == 0 and c_index == 0:
        if grid[r_index + 1][c_index] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index][c_index] == "#":
            numb_mine += 1

    elif r_index == 0 and (0 < c_index < number_of_cols):
        if grid[r_index][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index][c_index + 1] == "#":
            numb_mine += 1

    elif r_index == 0 and c_index == 4:
        if grid[r_index][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index] == "#":
            numb_mine += 1

    elif r_index == 1 and c_index == 0:
        if grid[r_index - 1][c_index] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index] == "#":
            numb_mine += 1

    elif r_index == 1 and (0 < c_index < number_of_cols):
        if grid[r_index][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index - 1] == "#":
            numb_mine += 1

    elif r_index == 1 and c_index == 4:
        if grid[r_index - 1][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index] == "#":
            numb_mine += 1
        if grid[r_index][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index] == "#":
            numb_mine += 1

    if r_index == 2 and c_index == 0:
        if grid[r_index - 1][c_index] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index] == "#":
            numb_mine += 1

    elif r_index == 2 and (0 < c_index < number_of_cols):
        if grid[r_index][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index - 1] == "#":
            numb_mine += 1

    elif r_index == 2 and c_index == 4:
        if grid[r_index - 1][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index] == "#":
            numb_mine += 1
        if grid[r_index][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index] == "#":
            numb_mine += 1

    elif r_index == 3 and c_index == 0:
        if grid[r_index - 1][c_index] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index] == "#":
            numb_mine += 1

    elif r_index == 3 and (0 < c_index < number_of_cols):
        if grid[r_index][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index - 1] == "#":
            numb_mine += 1

    elif r_index == 3 and c_index == 4:
        if grid[r_index - 1][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index] == "#":
            numb_mine += 1
        if grid[r_index][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index + 1][c_index] == "#":
            numb_mine += 1

    if r_index == 4 and c_index == 0:
        if grid[r_index - 1][c_index] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index][c_index + 1] == "#":
            numb_mine += 1

    elif r_index == 4 and (0 < c_index < number_of_cols):
        if grid[r_index][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index + 1] == "#":
            numb_mine += 1
        if grid[r_index][c_index + 1] == "#":
            numb_mine += 1

    elif r_index == 4 and c_index == 4:
        if grid[r_index][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index - 1] == "#":
            numb_mine += 1
        if grid[r_index - 1][c_index] == "#":
            numb_mine += 1

    return numb_mine

# With the enumerate function, a value is assigned to each row and the column inside each row.
# The grid index containing the assigned values is pass to the count_mines function.

for row_index, row_data in enumerate(grid):
    for col_index, col_data in enumerate(row_data):
        if col_data == "-":
            grid[row_index][col_index] = count_mines(row_index, col_index)


print("After mining:")

print_grid()
