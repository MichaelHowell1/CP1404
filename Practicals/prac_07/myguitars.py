"""
CP1404 Prac 7 - My Guitars

"""

from prac_06.guitar import Guitar


def main():
    """ """
    guitars = get_guitar_data()
    get_user_guitar(guitars)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def get_guitar_data():
    """ """
    guitars = []
    with open('guitars.csv', 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


def get_user_guitar(guitars):
    """ """
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        current_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(current_guitar)
        print(f"{guitar_name} ({guitar_year}) : {guitar_cost} added")
        guitar_name = input("Name: ")


main()
