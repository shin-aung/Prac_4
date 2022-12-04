"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    number_of_months = int(input("How many months? "))
    incomes = income_for_every_month(number_of_months)
    print(f"Income Report\n------------------")
    print_report(number_of_months, incomes)


def print_report(number_of_months, incomes):
    total_income = 0
    for month in range(0, number_of_months):
        total_income += incomes[month]
        print(f"Month {str(month + 1)} - Income: $ {incomes[month]:.2f}        Total: $ {total_income:.2f}")


def income_for_every_month(number_of_months):
    income_for_each_month = []
    for month in range(0, number_of_months, 1):
        monthly_income = float(input(f"Enter income for month {str(month)}: "))
        income_for_each_month.append(monthly_income)
    return income_for_each_month



main()