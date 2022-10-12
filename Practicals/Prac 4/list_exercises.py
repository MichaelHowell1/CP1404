"""
CP1404 Prac 4 - List Exercises
Program which takes a specified number of numbers and returns information from these.
The first, the last, the smallest, the largest and the average number is printed.
"""

total_numbers = int(input("How many numbers? "))
numbers = []
for number in range(total_numbers):
    number = float(input("Enter a number: "))
    numbers.append(number)
average_number = sum(numbers)/total_numbers

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average number is {average_number}")


# Section 2 - Security Checker
# Program to check username from user against a list of accepted usernames.

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Please enter your username: ")
access_granted = False
while not access_granted:
    if username in usernames:
        print("Access granted")
        access_granted = True
    else:
        print("Access denied")
        username = input("Please enter your username: ")

