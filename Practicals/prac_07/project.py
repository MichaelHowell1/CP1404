"""
CP1404 Prac 7 - Project

"""


class Project:
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
