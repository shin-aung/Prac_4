SMALLEST_NUMBER = 1
LARGEST_NUMBER = 45
NUMBER_OF_DIGITS_IN_EACH_LINE = 6
number_of_quick_picks = int(input("How many quick picks? "))
for number_of_columns in range(0, number_of_quick_picks, 1):
    random_numbers = []
    for digit_in_rows in range(0, NUMBER_OF_DIGITS_IN_EACH_LINE, 1):
        import random
        random_number = random.randint(SMALLEST_NUMBER, LARGEST_NUMBER)
        while random_number in random_numbers:
            random_number = random.randint(SMALLEST_NUMBER, LARGEST_NUMBER)
        random_numbers.append(random_number)
        print(random_number, end=" ")
    print()