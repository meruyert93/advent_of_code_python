from __future__ import annotations
import re
import pprint
from aoc_lib import ROW, COL
import aoc_lib as lib
import sys
sys.path.insert(0, '..')


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = ""

    def solve_part_1(self, raw_input):
        raw_input = raw_input.strip().split("\n")
        total_sum = 0
        for line in raw_input:
            # Find all digits in the line
            digits = [int(d) for d in line if d.isdigit()]

            if len(digits) >= 2:
                calibration_val = digits[0]*10 + digits[-1]
                total_sum += calibration_val

            elif len(digits) == 1:
                calibration_val = digits[0]*10 + digits[0]
                total_sum += calibration_val
            else:
                continue
        return total_sum

    def solve_part_2(self, raw_input):

        raw_input = (raw_input.replace("one", "one1one")
                     .replace("two", "two2two")
                     .replace("three", "three3three")
                     .replace("four", "four4four")
                     .replace("five", "five5five")
                     .replace("six", "six6six")
                     .replace("seven", "seven7seven")
                     .replace("eight", "eight8eight")
                     .replace("nine", "nine9nine")
                     )

        total_sum = self.solve_part_1(raw_input)

        return total_sum
