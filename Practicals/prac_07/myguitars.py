"""
CP1404 Prac 7 - My Guitars

"""

from prac_06.guitar import Guitar


def main():
    """ """
    guitars = get_guitar_data()
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


main()
