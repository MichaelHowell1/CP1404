
"""CP1404 Prac 1 Michael Howell"""

""" count odd numbers (0 to 20) """
for i in range(1, 21, 2):
    print(i, end=' ')
print()

""" count in 10s (0 to 100)"""
for i in range(0,101,10):
    print (i,end=' ')
print()


""" count down from 20 to 1"""
for i in range(20, 0, -1):
    print (i,end=' ')
print()

""" count user stars"""
stars = int(input("Enter number of stars: "))
for i in range(0, stars, 1):
    print( end= '*')
print()

""" count user stars increasing"""
for i in range(0, stars, 1):
    for o in range (0,i+1,1):
        print (end='*')
    print()