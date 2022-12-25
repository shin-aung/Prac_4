counts = []
ages = []
percentages = []
in_file = open("count", "r")
in_second_file = open("percentage", "r")
for line in in_file:
    count = line.rstrip().split(f"\t")
    counts.append(count[1])
    ages.append(count[0])
for lines in in_second_file:
    percentage = lines.rstrip().split(f"\t")
    counts.append(percentage[1])
for i in range(0, 25, 1):
    print(f"{counts[i]} of the interviewees who drink beers are {ages[i]}-year-old which is around {float(counts[i + 25]) * 100} percentage of the total interviewees.")
