"""
CP1404 Prac 9 - Band class
A class for a Band
"""


class Band:
    """Class of a band with a number of musicians and what instrument they are playing."""

    def __init__(self, band_name):
        """Initialise a Band instance."""
        self.band_name = band_name
        self.band_members = []

    def __str__(self):
        """Return a string showing the band with each member and their instruments."""
        return f"{self.band_name} ({', '.join(str(musician) for musician in self.band_members)})"

    def add(self, musician):
        """Add musicians to band."""
        self.band_members.append(musician)

    def play(self):
        """Return a string showing each member in the band and whether they are playing instrument."""
        return "\n".join(musician.play() for musician in self.band_members)
