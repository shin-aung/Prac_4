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


def run_test():
    ruby = Pointer_Arithmetic("Ruby", "Dynamic", True, 1995)
    python = Pointer_Arithmetic("Python", "Dynamic", True, 1991)
    visual_basic = Pointer_Arithmetic("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print("The languages whose are Ture:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

    print("The languages which has been used for thirty years or more:")
    for language in languages:
        if language.thirty_years_of_used():
            print(language.name)


if __name__ == '__main__':
    run_test()