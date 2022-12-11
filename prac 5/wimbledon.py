wimbledon_champions_counts = dict()
country_counts = dict()
wimbledon_champions = []
champions_countries = []
with open("wimbledon.csv", "r", encoding= "utf-8-sig") as in_file:
    for line in in_file:
        line = line.rstrip().split(",")
        champion = line[2]
        wimbledon_champions.append(champion)
        country = line[1]
        champions_countries.append(country)
    print("Wimbledon Champions:")
    for champion in wimbledon_champions:
        if champion in wimbledon_champions_counts:
            wimbledon_champions_counts[champion] += 1
        else:
            wimbledon_champions_counts[champion] = 1
    for wimbledon_champions_count in wimbledon_champions_counts:
        print(wimbledon_champions_count, ":", wimbledon_champions_counts[wimbledon_champions_count])
    for country in champions_countries:
        if country in country_counts:
            country_counts[country] += 1
        else:
            country_counts[country] = 1
    print(f"\nThese {len(country_counts)} have won Wimbledon:")
    for country in country_counts:
        print(country, end=", ")
in_file.close()