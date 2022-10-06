"""
CP1404 Prac 4 - Quick Picks
Simulate random "quick picks", 6 per line and user input for number of lines.
"""

import random

number_of_picks = int(input("How many quick picks? "))
picks_per_line = 6

for picks_line in range(number_of_picks):
    pick_numbers = []
    for picks in range(picks_per_line):
        number = random.randint(1, 45)
        while number in pick_numbers:
            number = random.randint(1, 45)
        pick_numbers.append(number)
    pick_numbers.sort()
    print(f" ".join("{:2}".format(number) for number in pick_numbers))
