"""
CP1404 Prac 4 - Subject Reader
Reads data from "subject_data.txt" file, saves the subject data then prints the data with context.
"""


def main():
    """Read data and prints it with context"""
    subject_data = get_data()
    print_subject_data(subject_data)


def get_data():
    """Read data in lines from files and save to nested list."""
    input_file = open("subject_data.txt")
    subject_data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(",")
        parts[2] = int(parts[2])
        subject_data.append(parts)
    input_file.close()
    return subject_data


def print_subject_data(data):
    """Print data for each subject from the nested list including:
    subject name, lecturer name and number of students for each class."""
    for class_number in range(len(data)):
        subject_name = data[class_number][0]
        lecturer_name = data[class_number][1]
        number_of_students = data[class_number][2]
        print(f"{subject_name} is taught by {lecturer_name} and has {number_of_students} students")


main()
