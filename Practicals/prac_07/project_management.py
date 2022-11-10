"""
CP1404 Prac 7 - Project Management

"""

filename = "projects.txt"
from prac_07.project import Project


def main():
    projects = read_project_data()
    for project in projects:
        print(project)
    menu = """Menu:
L - Load projects
S - Save projects 
D - Display projects
F - Filter projects by date
A - Add new project
U - Update project
Q - Quit
>>> """
    menu_choice = input(menu).upper()

    while menu_choice != "Q":
        if menu_choice == "L":
            projects = load_projects()
        elif menu_choice == "S":
            save_projects()
        elif menu_choice == "D":
            display_projects()
        elif menu_choice == "A":
            add_project()
        elif menu_choice == "F":
            filter_project()
        elif menu_choice == "U":
            update_project()
        else:
            print(f"Invalid menu choice")
        menu_choice = input(menu).upper()
    save_to_file(filename, projects)
    print(f"Thank you for using custom-built project management software.")


def load_projects():
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


main()
