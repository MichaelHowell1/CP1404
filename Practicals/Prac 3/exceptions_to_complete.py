""" CP1404 Prac 3 - Exceptions to Complete
A program which uses try function to find an appropriate integer to break the while not loop and print valid result.
"""


is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print(f"Valid result is: {result}")
