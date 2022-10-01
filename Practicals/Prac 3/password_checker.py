"""changed min length to 3 as cant have 2 characters for 3 different character conditions
if special character required need min length of 4"""
MIN_LENGTH = 3
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

menu = (f"""Please enter a valid password 
Your password must be between {MIN_LENGTH} and {MAX_LENGTH}, and contain:
\t1 or more uppercase characters
\t1 or more lowercase characters
\t1 or more numbers""")


def main():
    """Program to get and check a user's password."""
    print(menu)
    if SPECIAL_CHARS_REQUIRED:
        print(f" \t1 or more of the following special characters: {SPECIAL_CHARACTERS}")
    password = input("> ")
    while not is_valid_password(password):
        print(f"Invalid password! Please check password requirements and try again.")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: ")


def is_valid_password(password):

    if MIN_LENGTH > len(password) or len(password) > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isdigit():
            count_digit = count_digit + 1
        elif char.islower():
            count_lower = count_lower + 1
        elif char.isupper():
            count_upper = count_upper + 1
        elif char in SPECIAL_CHARACTERS:
            count_special = count_special + 1

    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False
    if SPECIAL_CHARS_REQUIRED:
        if count_special == 0:
            return False

    return True

main()
