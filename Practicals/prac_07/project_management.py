"""
CP1404 Prac 7 - Project Management
Store and view information about a project or number of projects
Estimated time: 2hrs
Actual time: 3hrs - incomplete
"""

from prac_07.project import Project
import datetime

filename = "projects.txt"


def main():
    """Program to load, save, display, sort, add and update projects in a project file"""
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
        try:
            if menu_choice == "L":
                projects = load_projects()
            elif menu_choice == "S":
                save_projects(projects)
            elif menu_choice == "D":
                display_projects(projects)
            elif menu_choice == "A":
                add_project(projects)
            elif menu_choice == "F":
                filter_projects(projects)
            elif menu_choice == "U":
                update_projects(projects)
            else:
                print(f"Invalid menu choice")
            menu_choice = input(menu).upper()
        except UnboundLocalError:
            print("Please load a file first")
            menu_choice = input(menu).upper()
    print(f"Thank you for using custom-built project management software.")


def load_projects():
    """Ask user for filename and load project data from that file"""
    projects = []
    user_filename = input(f"filename\n>>> ")
    try:
        with open(user_filename, 'r') as in_file:
            in_file.readline()
        chosen_file = user_filename
    except FileNotFoundError:
        print(f"File not found using '{filename}'")
        chosen_file = filename

    with open(chosen_file, 'r') as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects


def save_projects(projects):
    """Ask user for filename and saves project data to that file"""
    user_filename = input(f"filename\n>>> ")
    with open(user_filename, 'w') as out_file:
        print(f"Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=out_file)
        for project in projects:
            print(
                f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                f"{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display projects sorted by priority in incomplete and complete sections"""
    complete_project = []
    incomplete_project = []
    projects.sort()
    for project in projects:
        current_project = project
        if project.is_complete():
            complete_project.append(current_project)
        else:
            incomplete_project.append(current_project)
    print(f"Incomplete projects:")
    for project in incomplete_project:
        print(f"\t{project}")
    print(f"Complete projects:")
    for project in complete_project:
        print(f"\t{project}")


def add_project(projects):
    """Add new project to list"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = int(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    current_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(current_project)


def filter_projects(projects):
    """Show projects after user selected date"""
    filter_criteria = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(filter_criteria, "%d/%m/%Y").date()
    for project in projects:
        date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
        if date > filter_date:
            print(project)


def update_projects(projects):
    """Update project completion and priority for a user selected project"""
    for project_number, project in enumerate(projects):
        print(f"{project_number} {project}")
    is_finished = False
    while not is_finished:
        try:
            project_choice = int(input("Project choice: "))
            for project_number, project in enumerate(projects):
                if project_choice == project_number:
                    print(project)
                    completion_percentage = int(input("New Percentage: "))
                    priority = int(input("New Priority:"))
                    project.completion_percentage = completion_percentage
                    project.priority = priority
                else:
                    raise KeyError
        except ValueError:
            print("Invalid input, please input number")
        except KeyError:
            print(f"Please choose a valid project number from the list")


main()
