"""
CP1404 Prac 7 - Programming Language
Programming Language class with tests.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, arithmetic, year):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name  # name of language
        self.typing = typing  # dynamic or static typing
        self.reflection = reflection  # reflective typing
        self.year = year  # year released
        self.arithmetic = arithmetic  # pointer arithmetic

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, Pointer Arithmetic=" \
               f"{self.arithmetic}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

    def is_pointer_arithmetic(self):
        """Determine if language performs pointer arithmetic operations"""
        return self.arithmetic is True


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, False, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, False, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, False, 1991)
    c_sharp = ProgrammingLanguage("C#", "Static", True, True, 2000)

    languages = [ruby, python, visual_basic, c_sharp]
    print(python)
    print(c_sharp)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    run_tests()
