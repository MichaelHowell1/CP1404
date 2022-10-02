""" CP1404 Prac 3 - Files
Writes and reads specific data to .txt files in the same directory."""

""" Writing the name to file"""
name = str(input("Please enter your name: "))
output_file = "name.txt"
out_file = open('name.txt', 'w')
print(f"{name}", file=out_file)
out_file.close()

"""Reading the name from the file"""
in_file = open('name.txt', 'r')
name = in_file.readline()
print(f"Your name is {name}")
in_file.close()

"""Reading the two numbers from file"""
in_file = open('numbers.txt', 'r')
number1 = int(in_file.readline())
number2 = int(in_file.readline())
total_number = number1 + number2
print(f"Number 1 + Number 2 = {total_number}")
in_file.close()

"""Reading all numbers from file"""
in_file = open('numbers.txt', 'r')
total_number = 0

for line_number in in_file:
    number = int(line_number)
    total_number = total_number + number
print(f"The total addition of the numbers in numbers.txt file = {total_number}")
in_file.close()
