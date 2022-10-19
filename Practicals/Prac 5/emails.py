"""
CP1404 Prac 5 - Emails
Add unique emails to dictionary
Estimate: 1hr
Actual
"""


def main():
    """ Dictionary of emails to names."""
    email_to_name = {}
    email = input("Email: ")
    name = extract_name(email)


def extract_name(email):
    """extract name from email"""
    username = email.split("@")[0]
    name_parts = username.split(".")
    name = " ".join(name_parts).title()
    return name


main()
