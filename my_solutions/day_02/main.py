from pprint import pprint
from warnings import catch_warnings
import aoc_lib as lib
import sys
sys.path.insert(0, '..')


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = ""

    def is_game_possible(self, game_record):
        red_cubes = 12
        green_cubes = 13
        blue_cubes = 14

        for draw in game_record:
            if draw['red'] > red_cubes or draw['green'] > green_cubes or draw['blue'] > blue_cubes:
                return False
        return True

    def get_draw_records(self, draws):
        draw_records = []
        for draw in draws.split('; '):
            draw_record = {'red': 0, 'green': 0, 'blue': 0}
            for color_info in draw.split(', '):
                number, color = color_info.split(' ')
                draw_record[color] += int(number)
            draw_records.append(draw_record)
        return draw_records

    def get_minimum_draw_records(self, draws):
        min_draw_record = {'red': 0, 'green': 0, 'blue': 0}
        for draw in draws.split('; '):
            draw_record = {'red': 0, 'green': 0, 'blue': 0}
            for color_info in draw.split(', '):
                number, color = color_info.split(' ')
                draw_record[color] = int(number)
                min_draw_record[color] = max(
                    min_draw_record[color], draw_record[color])
        return min_draw_record

    def solve_part_1(self, raw_input):
        games = raw_input.split('\n')

        sum = 0

        for game in games:
            game_id, draws = game.split(': ')
            game_id = int(game_id.replace('Game ', ''))

            draw_records = self.get_draw_records(draws)

            if self.is_game_possible(draw_records):
                sum += game_id

        return sum

    def solve_part_2(self, raw_input):
        games = raw_input.strip().split('\n')
        total_power_sum = 0

        for game in games:
            _, draws = game.split(': ')
            min_draw_records = self.get_minimum_draw_records(draws)

            power = (min_draw_records['red'] *
                     min_draw_records['green'] *
                     min_draw_records['blue'])
            total_power_sum += power

        return total_power_sum
