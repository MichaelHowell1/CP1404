"""
CP1404 Prac 6 - Guitars


Estimate: 30 minutes
Actual:
"""
from prac_06.guitar import Guitar
from operator import attrgetter

def main():
    """ Notes"""

    guitars = []
    """    guitar_name = input("Name: ")
    while guitar_name != "":

        guitar_year = input("Year: ")
        guitar_cost = input("Cost: $")
        current_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(current_guitar)
        print(f"{guitar_name} ({guitar_year}) : {guitar_cost} added")
        guitar_name = input("Name: ")"""
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))



    for i, guitar in enumerate(guitars, 1):

        vintage_string = "(vintage)" if guitar.is_vintage() is True else ""
        print(f"Guitar {i}: {guitar.name:>{largest_word_length}} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")




main()
