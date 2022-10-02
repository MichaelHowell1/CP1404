""" CP1404 Prac 3 - String Formatting
Program takes variables and prints it using an f string in this cast the year, name and cost of a guitar.
The final section uses f string to print set numbers"""

""" variables, could be an input with a menu"""
name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

"""convert cost to integer to remove decimal"""
cost = int(cost)

""" printing the year, name and cost using f-string formatting """
print(f"{year} {name} for about ${cost}!")
print()

""" printing numbers in specific range at intervals of 50. (0, 50, 100, 150) 
right justified using (:3) in a f-string format"""
for number in range(0, 151, 50):
    print(f"{number:3}")