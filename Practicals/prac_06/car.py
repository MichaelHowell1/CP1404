"""
CP1404 Prac 6 - Car class
Class for a car used in the "used car" simulation
"""


class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):
        """Initialise a Car instance.
        where:
            name: string, name assigned to car
            fuel: float, one unit of fuel drives one kilometre
            odometer: distance car has travelled
        """
        self.name = name
        self.fuel = fuel
        self._odometer = 0

    def add_fuel(self, amount):
        """Add amount to the car's fuel."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance

    def __str__(self):
        """Change class output into readable string."""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"
