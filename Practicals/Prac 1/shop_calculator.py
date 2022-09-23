
"""CP1404 Prac 1 Michael Howell"""

items = int(input("Enter total number of items: "))
total = 0
for i in range(1, items+1):
    price = float(input("Enter price of item: "))
    while price <= 0:
        price = float(input("Please enter valid price (number above zero)"))
    total = total + price

if total > 100:
    total = total * .9
items = int(items)


print ("The total price for", items,"items is", "{:.2f}".format(total))

