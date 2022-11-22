"""
CP1404 Prac 9 - Taxi test
Test model the taxi class
"""

from prac_09.taxi import Taxi


def main():
    """Client test code for a taxi"""
    # Initial fare
    my_taxi = Taxi("Prius 1", 100, 1.23)
    my_taxi.drive(40)
    print(f"{my_taxi}\nCurrent fare: ${my_taxi.get_fare()}")
    # Start a new fare
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(f"{my_taxi}\nCurrent fare: ${my_taxi.get_fare()}")


main()
