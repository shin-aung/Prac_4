"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


# if __name__ == "__main__":
#     run_tests()

class Pointer_Arithmetic:

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.reflection is True

    def thirty_years_of_used(self):
        return 2022 - int(self.year) > 30

    def __repr__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def __str__(self):
        return f"The name of the language is {self.name}. The typing of the langauge is {self.typing} and the reflection is {self.reflection}. The language first appeared in the year of {self.year}."

def run_test():
    ruby = Pointer_Arithmetic("Ruby", "Dynamic", True, 1995)
    python = Pointer_Arithmetic("Python", "Dynamic", True, 1991)
    visual_basic = Pointer_Arithmetic("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    for language in languages:
        print(language)

    print("The languages whose reflection are Ture:")
    for language in languages:
        if language.is_dynamic():
            print(language.name + "Dynamic" + language.typing)

    print("The languages which has been used for thirty years or more:")
    for language in languages:
        if language.thirty_years_of_used():
            print(language.name)


if __name__ == '__main__':
    run_test()