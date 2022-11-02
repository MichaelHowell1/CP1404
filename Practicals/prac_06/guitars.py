"""
CP1404 Prac 6 - Guitars


Estimate: 30 minutes
Actual: 2hrs
"""
from prac_06.guitar import Guitar


def main():


    guitars = []
    guitar_name = input("Name: ")
    while guitar_name != "":

        guitar_year = input("Year: ")
        guitar_cost = input("Cost: $")
        current_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(current_guitar)
        print(f"{guitar_name} ({guitar_year}) : {guitar_cost} added")
        guitar_name = input("Name: ")
    """    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))"""

    largest_word_length = 0
    for guitar in guitars:
        if largest_word_length < len(guitar.name):
            largest_word_length = len(guitar.name)

    for guitar_number, guitar in enumerate(guitars, 1):

        vintage_string = "(vintage)" if guitar.is_vintage() is True else ""
        print(f"Guitar {guitar_number}: {guitar.name:>{largest_word_length}} ({guitar.year}), worth "
              f"${guitar.cost:10,.2f} {vintage_string}")




main()
