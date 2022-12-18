class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        result = self.detail(name, typing, reflection, year)
        print(result)


    def detail(self, name, typing, reflection, year):
        return f"{name}, {typing} Typing, Reflection={reflection}, First appeared in {year}"

    def dynamic(self, name, typing):
        if typing == True:
            return name
        else:
            return ""
