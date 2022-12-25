class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __repr__(self):
        return f"The name of the guitar is {self.name} which is made in {self.year} and the cost is ${self.cost}."

    def __lt__(self, other):
        return self.year < other.year


def main():
    guitars = []
    in_file = open("guitars.csv", "r")
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(",")
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
    in_file.close()

    name_of_guitar = input("Name of Guitar:  ")
    year_of_guitar = input("Year when the guitar was made:  ")
    cost_of_guitar = input("Cost of Guitar:  ")
    user_guitar = Guitar(name_of_guitar, int(year_of_guitar), float(cost_of_guitar))
    guitars.append(user_guitar)

    guitars.sort()
    for guitar in guitars:
        print(guitar)

    out_file = open("guitars.csv", "a")
    print(f"{name_of_guitar},{year_of_guitar},{cost_of_guitar}", file=out_file)
    out_file.close()


main()