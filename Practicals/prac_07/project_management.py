"""
CP1404 Prac 7 - Project Management

"""

from prac_07.project import Project
filename = "projects.txt"


def main():
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
            for project in projects:
                print(project)
        elif menu_choice == "S":
            save_projects(projects)
        elif menu_choice == "D":
            display_projects(projects)
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


def save_projects(projects):
    with open(filename, 'w') as out_file:
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage")
        for project in projects:
            print(
                f"{project.name}\t,{project.start_date}]\t,{project.priority}\t,{project.cost_estimate}\t,"
                f"{project.completion_percentage}", file=out_file)


def display_projects(projects):
    complete_project = []
    incomplete_project = []
    projects.sort()
    for project in projects:
        current_project = project
        if project.is_complete() is True:
            complete_project.append(current_project)
        else:
            incomplete_project.append(current_project)
    print(f"Incomplete projects:")
    for project in incomplete_project:
        print(f"\t{project}")
    print(f"Complete projects:")
    for project in complete_project:
        print(f"\t{project}")


main()
