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
    guitars.sort()
    for guitar in guitars:
        print(guitar)



main()