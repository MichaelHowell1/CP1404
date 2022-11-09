"""
CP1404 Prac 7 - Project Management

"""

filename = "projects.txt"
from prac_07 import Project


def main():
    projects = read_project_data()
    menu = """Menu:
L - Load projects
S - Save projects 
D - Display projects
F - Filter projects by date
A - Add new project
U - Update project
Q - Quit
>>> """


def read_project_data():
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip()
            project = Project(parts[0], int(parts[1]), float(parts[2]))
            projects.append(project)
    return projects


main()
