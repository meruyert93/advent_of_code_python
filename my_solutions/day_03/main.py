from pprint import pprint
import aoc_lib as lib
import sys
sys.path.insert(0, '..')


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = ""

    def is_symbol(self, char):
        return char != '.'

    def is_adjacent_to_symbol(self, grid, num_str, start_row, start_col):
        """ Check if the number is adjacent to a symbol. """
        end_col = start_col + len(num_str) - 1
        for i in range(start_row-1, start_row+2):
            for j in range(start_col-1, end_col+2):
                if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and self.is_symbol(grid[i][j]):
                    return True
        return False

    def solve_part_1(self, raw_input):
        grid = [list(row) for row in raw_input.split('\n')]
        total = 0

        length = len(grid)

        for i in range(length):
            j = 0
            while j < length:
                if grid[i][j].isdigit():
                    num_str = ''
                    # Extract the full number
                    while j < len(grid[i]) and grid[i][j].isdigit():
                        num_str += grid[i][j]
                        j += 1

                    if self.is_adjacent_to_symbol(grid, num_str, i, j - len(num_str)):
                        total += int(num_str)
                else:
                    j += 1

        return total

    def solve_part_2(self, raw_input):
        ...
