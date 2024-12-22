def print_grid(grid):
    """Prints the Sudoku grid in a readable format."""
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid(grid, row, col, num):
    """Checks if placing a number in a cell is valid."""
    # Check the row
    for x in range(9):
        if grid[row][x] == num:
            return False

    # Check the column
    for x in range(9):
        if grid[x][col] == num:
            return False

    # Check the 3x3 subgrid
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(grid):
    """Solves the Sudoku puzzle using backtracking."""
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:  # Empty cell
                for num in range(1, 10):  # Numbers 1-9
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0  # Undo the move
                return False
    return True

if __name__ == "__main__":
    # Example Sudoku puzzle (0 represents empty cells)
    sudoku_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print("Unsolved Sudoku:")
    print_grid(sudoku_grid)

    if solve_sudoku(sudoku_grid):
        print("\nSolved Sudoku:")
        print_grid(sudoku_grid)
    else:
        print("\nNo solution exists for the given Sudoku puzzle.")

