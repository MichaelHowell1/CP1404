"""
CP1404 Prac 6 - Guitar


Estimate: 30 minutes
Actual:
"""
from prac_06.guitar import Guitar

def main():

    gibson = Guitar("Gibson_L_-_5_CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013)
    print(gibson)
    print(another_guitar)


main()