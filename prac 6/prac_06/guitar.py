class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.year = year
        self.cost = cost
        print(self.is_vintage(year))

    def cost(self, amount):
        self.cost += amount

    def get_age(self, year):
        return 2022 - int(year)

    def is_vintage(self, year):
        if 2022 - int(year) >= 50:
            return True
        else:
            return False

    def cost_of_guitar(self, name, year, cost):
        return f"{name} ({year}) : ${cost}"

    def output(self, name, year, cost):
        if 2022 - year >= 50:
            return f"{name} ({year}), worth $ {cost} (vintage)"
        else:
            return f"{name} ({year}), worth $ {cost}"