""" CP1404 Prac 3 - Exceptions Demo
Answers to questions about the try function below."""

"""
1. When will a ValueError occur?
If either the numerator or denominator are not integers

2. When will a ZeroDivisionError occur?
When the denominator = 0

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Could add an if statement that if denominator = 0 then it outputs the fraction as = 0
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    """Question 3 code where if denominator is 0 then it changes fraction to 0, otherwise allows calculation as usual"""
    if denominator == 0:
        fraction = 0
    else:
        fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")