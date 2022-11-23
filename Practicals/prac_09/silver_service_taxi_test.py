"""
CP1404 Prac 9 - Silver Service Taxi test
Test for the Silver Service Taxi class
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Client test code for a taxi"""

    fuel = 200
    fanciness = 2
    drive_distance = 18
    my_taxi = SilverServiceTaxi("Hummer", fuel, fanciness)
    my_taxi.drive(drive_distance)
    print(f"{my_taxi}\nThe cost was ${my_taxi.get_fare():.2f}")


main()
