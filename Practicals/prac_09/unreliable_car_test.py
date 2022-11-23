"""
CP1404 Prac 9 - Unreliable car test
Test model of the unreliable class
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Client test code for an unreliable car"""

    drive_distance = 10
    reliability = 50
    fuel = 100

    my_car = UnreliableCar("Car", fuel, reliability)
    for attempt_number in range(1, 11):
        my_car.drive(drive_distance)
    print(f"{my_car.name} attempted {attempt_number} times to drive 10km which resulted in:")
    print(f"{my_car}")


main()
