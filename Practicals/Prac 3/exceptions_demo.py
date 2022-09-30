"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
If either the numerator or denominator are not integers

2. When will a ZeroDivisionError occur?
When the denominator = 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Could add an if statement that if denominator = 0 then it asks for denominator again for valid number,
    would be viable to fix value error also.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")