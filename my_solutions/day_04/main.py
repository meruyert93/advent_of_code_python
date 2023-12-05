from pprint import pprint
import aoc_lib as lib
import sys
sys.path.insert(0, '..')


class DayPuzzleSolver():
    def __init__(self):
        self.delimiter = ""

    def parse_card(self, card):
        card = card.split(': ')
        card = card[1]

        winning_nums, my_nums = card.split(' | ')
        winning_nums = set(map(int, winning_nums.split()))
        my_nums = list(map(int, my_nums.split()))
        return winning_nums, my_nums

    def count_matches(self, winning_nums, my_nums):
        count = 0
        for num in my_nums:
            if num in winning_nums:
                count += 1

        return count

    def solve_part_1(self, raw_input):
        total_points = 0

        raw_input = raw_input.split('\n')

        for card in raw_input:
            winning_nums, my_nums = self.parse_card(card)
            matches = self.count_matches(winning_nums, my_nums)
            points = 1 if matches > 0 else 0

            for _ in range(1, matches):
                points *= 2
            total_points += points
        return total_points

    def solve_part_2(self, original_cards):
        original_cards = original_cards.split('\n')
        # Initialize queue with indices of all original cards
        queue = list(range(len(original_cards)))
        processed_cards = 0  # Counter for total number of processed cards

        while queue:
            card_index = queue.pop(0)  # Get the next card index to process
            processed_cards += 1  # Increment the processed cards counter

            # Check for matches in the current card
            winning_numbers, your_numbers = self.parse_card(
                original_cards[card_index])
            matches = self.count_matches(winning_numbers, your_numbers)

            # For each match, add the index of the next card to the queue
            for i in range(1, matches + 1):
                if card_index + i < len(original_cards):
                    queue.append(card_index + i)

        return processed_cards
