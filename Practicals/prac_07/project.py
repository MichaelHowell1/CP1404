"""
CP1404 Prac 7 - Project
Class for project
"""
completion_criteria = 100


class Project:
    """Represent a Project object."""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Create a project"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Change class output into readable string."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, " \
               f"completion: {self.completion_percentage}% "

    def __lt__(self, other):
        """Sorts project by priority"""
        return self.priority < other.priority

    def is_complete(self):
        """Checks if completion percentage is 100%"""
        return self.completion_percentage >= completion_criteria
