"""
CP1404 Prac 4 - Quick Picks
Simulate random "quick picks"
"""

import random

number_of_picks = int(input("How many quick picks? "))
picks_per_line = 6

for temp in range(number_of_picks):
    pick_numbers = []
    for temp in range(picks_per_line):
        number = random.randint(1, 45)
        pick_numbers.append(number)
    pick_numbers.sort()
    print(f" ".join("{:2}".format(number) for number in pick_numbers))
print(pick_numbers)
