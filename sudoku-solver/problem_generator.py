# Generates grids for the Sudoku solver to solve.\
import random
from solver_backtracking import is_valid

def generate_problem():
    grid = initialise_grid()
    fill_diagonal_boxes(grid)
    fill_remaining(grid, 0, 0)
    remove_numbers(grid, random.randint(20, 40))
    return grid

def initialise_grid():
    return [[0 for _ in range(9)] for _ in range(9)]

# diagonal boxes are independent of each other, so we can fill them first
def fill_diagonal_boxes(grid):
    for i in range(0, 9, 3):
        fill_box(grid, i, i)

def fill_box(grid, start_row, start_col):
    num_list = list(range(1, 10))
    random.shuffle(num_list)
    for i in range(3):
        for j in range(3):
            grid[start_row + i][start_col + j] = num_list.pop()

def fill_remaining(grid, row, col):
    pass

def remove_numbers(grid, count):
    pass

base_grid = generate_problem()
