"""
CP1404 Prac 4 - Total Income
Cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many number of months? "))

    for month in range(1, number_of_months + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print_report(incomes)


def print_report(incomes):
    """Print report for Month, income and total using incomes list"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(len(incomes)):
        income = incomes[month]
        total += income
        print(f"Month {month+1} - Income: ${income:10.2f} - Total: ${total:10.2f}")


main()
