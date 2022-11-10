"""
CP1404 Prac 7 - My Guitars
Store and view guitars from file
Estimate time: 1hr
Actual timeL 1hr
"""

from prac_06.guitar import Guitar

filename = 'guitars.csv'


def main():
    """Loads and displays guitar information from file then asks user for guitar information and saved to file when
    complete"""
    guitars = get_guitar_data()
    display_guitars(guitars)
    get_user_guitar(guitars)
    guitars.sort()
    save_guitars(guitars)
    print(f"Guitars have been saved")


def get_guitar_data():
    """Loads guitars from file"""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Displays guitars"""
    for guitar in guitars:
        print(guitar)


def get_user_guitar(guitars):
    """Asks user for guitar and stores in list"""
    guitar_name = input("Name: ")
    while guitar_name != "":
        guitar_year = int(input("Year: "))
        guitar_cost = float(input("Cost: $"))
        current_guitar = Guitar(guitar_name, guitar_year, guitar_cost)
        guitars.append(current_guitar)
        print(f"{guitar_name} ({guitar_year}) : {guitar_cost} added")
        guitar_name = input("Name: ")


def save_guitars(guitars):
    """Saves guitar information to file"""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
