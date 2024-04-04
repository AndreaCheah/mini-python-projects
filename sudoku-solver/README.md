# Breakdown of the Game

### 1. Sudoku Rules

a) Sudoku is played on a 9x9 grid, and the grid is divided into 9 3x3 subgrids.  
b) The objective is to fill the grid so that each row, each column, and each of the 9 3x3 subgrids contains all of the digits from 1 to 9.

### 2. Sudoku Grid

The grid is represented as a 9x9 2D list. `0` is used to represent empty cells.

### 3. Outline of the Algorithm
Backtracking (brute-force and depth-first search) is used.
1. Base Case  
   No more empty cells.
2. Recursive Case  
   Find the next first empty cell.  
3. Try a digit at the empty cell  
Try a digit from `1`-`9`. Start from the digit `1`. Check if the digit follows the rules of Sudoku (row, column, subgrid). If valid, save the digit into the empty cell. If not valid, try next digit.  
4. If all the digits from `1`-`9` violate the Sudoku rules for this cell, backtrack to previous cell.