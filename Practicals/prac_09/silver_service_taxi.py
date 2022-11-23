"""
CP1404 Prac 9 - Silver Service Taxi Class
A class for a Silver Service Taxi, derived from parent class taxi
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness and a flagfall."""

    flagfall = 4.5  # Extra charge for each new fare

    def __init__(self, name, fuel, fanciness):
        """Initialise a Silver Service Taxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a string for SilverServiceTaxi, based on taxi + flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}\nCurrent fare: ${self.get_fare():.2f}"

    def get_fare(self):
        """Get the current fare."""
        return super().get_fare() + self.flagfall
