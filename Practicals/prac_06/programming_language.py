"""
CP1404 Prac 6 - Programming Language
Class of programming languages

Estimate: 30 minutes
Actual: 35 minutes
"""


class ProgrammingLanguage:
    """Store data about a programming language"""

    def __init__(self, name="", typing="", reflection="", year=""):
        """Initialise a ProgramingLanguage"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the ProgrammingLanguage has dynamic typing"""
        return self.typing == "Dynamic"

    def __str__(self):
        """Change class output into readable string."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
