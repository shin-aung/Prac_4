from guitar import Guitar
print("My guitars!")
for i in range(1,4):
    name = input("Name: ")
    year = input("Year: ")
    cost = input("cost: ")
    guitar_i = Guitar(name, int(year), float(cost))
    print(f"{Guitar.output(name, name, int(year), cost)}")