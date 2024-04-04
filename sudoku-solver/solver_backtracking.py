from problem_generator import generate_problem
from test_cases import test_cases

def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))
    print("\n")

def find_first_empty_cell(grid):
    for r in range(len(grid)):
        for c in range(len(grid[0])):
           if grid[r][c] == 0:
               return r, c 
    return None

def is_valid(grid, row, col, num):
    # check for same number in row, column, and subgrid
    for c in range(len(grid[0])):
        if grid[row][c] == num:
            return False
    for r in range(len(grid)):
        if grid[r][col] == num:
            return False
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True

def solve_sudoku(grid):
    # print_grid(grid)
    empty = find_first_empty_cell(grid)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):  # recurse till no more empty cells
                return True # puzzle solved
            grid[row][col] = 0  # if unsolvable, reset the cell and try next number 
    return False    # no number is valid in this cell, need to backtrack to previous cells

def test_solve_sudoku():
    for index, case in enumerate(test_cases):
        puzzle = case["puzzle"]
        expected = case["expected"]
        assert solve_sudoku(puzzle), f"According to the solver algorithm, no solution exists for puzzle {index+1}"
        assert puzzle == expected, f"Solution does not match expected for puzzle {index+1}"
        print(f"Puzzle {index+1} passed.")

if __name__ == "__main__":
    # Define a sample Sudoku puzzle
    # puzzle = generate_grid()
    
    test_solve_sudoku()

    # if solve_sudoku(puzzle):
    #     print("Sudoku puzzle solved successfully:")
    #     print_grid(puzzle)
    # else:
    #     print("No solution exists.")
    #     print_grid(puzzle)