"""
CP1404 Prac 6 - Languages
Determine whether language is dynamic

Estimate: 30 minutes
Actual: 35 minutes
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Use ProgrammingLanguage to find dynamic typing languages"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [python, ruby, visual_basic]

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
