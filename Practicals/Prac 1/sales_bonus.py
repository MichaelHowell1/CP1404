
"""CP1404 Prac 1 Michael Howell"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales <1000:
        bonus = sales * .1
        print("bonus is {:.2f}".format(bonus))
    elif sales >=1000:
        bonus = sales * .15
        print("bonus is {:.2f}".format(bonus))
    else:
        print("Please input a number")
    sales = float(input("Enter sales: $"))
