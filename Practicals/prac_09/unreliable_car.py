"""
CP1404 Prac 9 - Unreliable Car Class
A class for an UnreliableCar, derived from parent class car
"""

import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but only drive if random reliability is greater than car reliability."""
        reliability = random.randint(0, 100)
        if reliability < self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven



