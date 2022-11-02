"""
CP1404 Prac 6 - Guitars


Estimate: 30 minutes
Actual:
"""
from prac_06.guitar import Guitar


def main():

    """ Notes
    category = "adult" if age >= 18 else "child"
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    for i, guitar in enumerate(guitars, 1):
        # do something with i (the index) and guitar (the element)"""

    guitars = []
    guitar_name = input("Name: ")
    while guitar_name != "":

        guitar_year = input("Year: ")
        guitar_cost = input("Cost: $")
        current_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(current_guitar)
        print(f"{guitar_name} ({guitar_year}) : {guitar_cost} added")
        guitar_name = input("Name: ")


main()
