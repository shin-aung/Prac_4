from guitar import Guitar
name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
first_guitar = Guitar(name, year, cost)
another_guitar = Guitar("Another Guitar, 2013, 10000")
print(f"My guitar: {name}, first made in {year}")
print(f"Gibson L-5 CES get_age()  {first_guitar.get_age(int(year))}")
print(f"Another Guitar get_age()  {another_guitar.get_age(int(2013))}")
print(f"Gibson L-5 CES is_vintage()  {first_guitar.is_vintage(int(year))}")
print(f"Another Guitar is_vintage()  {another_guitar.is_vintage(int(2013))}")