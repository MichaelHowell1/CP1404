password = int(input("Please enter a 10 digit password: "))
stars = password
star_number = len(str(stars))

while star_number != "Q":
    if star_number == 10:
        print("**********")
        star_number = "Q"
    else:
        password = input("Please enter a 10 digit password: ")
        stars = password
        star_number = len(str(stars))
