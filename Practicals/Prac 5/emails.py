"""
CP1404 Prac 5 - Emails
Add unique emails to dictionary with their name

Estimate: 1 hour
Actual: 48 minutes
"""


def main():
    """Dictionary of emails to names."""
    email_to_name = {}
    email = input("Email: ")

    while email != "":
        name = extract_name(email)
        email_to_name[email] = check_name(name)
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract name from email"""
    username = email.split("@")[0]
    name_parts = username.split(".")
    name = " ".join(name_parts).title()
    return name


def check_name(name):
    """Check if name is correct with user"""
    check = input(f"Is your name {name}? (Y/N)").upper()
    if check != "Y" and check != "":
        name = input("Name: ").title()
    return name


main()
