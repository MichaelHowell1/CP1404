"""
CP1404 Prac 4 - Quick Picks
Simulate random "quick picks", 6 per line and user input for number of lines.
"""

import random

number_of_picks = int(input("How many quick picks? "))
picks_per_line = 6

print("Your quick picks are:")
for pick_line in range(number_of_picks):
    pick_numbers = []
    for number in range(picks_per_line):
        number = random.randint(1, 45)
        while number in pick_numbers:  # ensures no repeating numbers in pick line
            number = random.randint(1, 45)
        pick_numbers.append(number)
    pick_numbers.sort()  # sorts into ascending order
    print(" ".join("{:2}".format(number) for number in pick_numbers))  # formats neatly
