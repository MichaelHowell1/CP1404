"""
CP1404 Prac 6 - Guitar
Class for guitar

Estimate: 30 minutes
Actual (guitar test): 34 minutes
Actual (guitars) = 2 hrs 30 minutes
"""

current_year = 2022
vintage_criteria = 50


class Guitar:
    """Store data about a guitar"""
    def __init__(self, name="", year=0, cost=0):
        """Create a guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Change class output into readable string."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        """Get age of guitar"""
        return current_year - self.year

    def is_vintage(self):
        """Determine if guitar is vintage"""
        return self.get_age() >= vintage_criteria
