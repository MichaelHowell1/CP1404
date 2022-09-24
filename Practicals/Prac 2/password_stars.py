def main():

    star_number = get_password()

    print_number(star_number)


def print_number(star_number):
    while star_number != "Q":
        if star_number == 10:
            print("*" * 10)
            star_number = "Q"
        else:
            password = input("Please enter a 10 digit password: ")
            stars = password
            star_number = len(str(stars))


def get_password():
    password = input("Please enter a 10 digit password: ")
    stars = password
    star_number = len(str(stars))
    return star_number


main()