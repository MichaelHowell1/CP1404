"""
CP1404 Prac 4 - List Comprehensions
Further practice of list compressions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing the initials
# this splits each name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)

# this example uses filtering to select only the names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)

# and here's the join string method being used to create a single string from the names like:
# 'Ada Alan Angel Bob Jimi'
print(" ".join(sorted(names)))

"""
TODO section below
"""

"""Print the full names in lower case"""
lowercase_full_names = [full_names.lower() for full_names in full_names]
print(lowercase_full_names)

"""Convert the "almost numbers" to integers"""
almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
numbers = [int(almost_number) for almost_number in almost_numbers]
print(numbers)

"""Finds numbers greater than 9 from the almost number list"""
numbers_above_nine = [number for number in numbers if number > 9]
print(numbers_above_nine)

"""Finds names above 11 characters and prints the lastnames as a string """
names_above_eleven = [full_names for full_names in full_names if len(full_names) > 11]
last_names = [names_above_eleven.split()[1] for names_above_eleven in names_above_eleven]
print(", ".join(sorted(last_names)))
