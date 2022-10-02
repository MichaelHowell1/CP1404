""" CP1404 Prac 3 - Capitalist Conrad
Simulates a basic stock price.
It starts at the defined starting price and every timestep the random function is run to determine
if there is increase or decrease to the price.
Once the price reaches the upper or lower limit it breaks the while function and stops the code.
The starting price, change and limits are defined prior to the while function.
"""

import random

OUTPUT_FILE = "conrad_output.txt"
out_file = open(OUTPUT_FILE, 'w')

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
number_of_days = 0
price = INITIAL_PRICE

print(f"Starting price: {price:.2f}", file=out_file)


while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0

    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    number_of_days = number_of_days + 1

    price *= (1 + price_change)
    print(f"On day {number_of_days} price is: ${price:.2f}", file=out_file)
out_file.close()
