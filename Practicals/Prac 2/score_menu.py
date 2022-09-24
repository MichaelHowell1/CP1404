def main():

    menu = """Please choose one of the following options using the first letter
(S)core to see your grade or
(Q)uit"""
    print(menu)
    choice = input("Choice:").upper()
    while choice != "Q":
        if choice == "S":
            score = get_score()

            if score > 100:
                get_score()

            elif score < 0:
                get_score()
            print_grade(score)
        else:
            print("Invalid option")
        print()

        print(menu)
        choice = input("Choice:").upper()


def print_grade(score):
    if score >= 90:
        print("Your grade is: Excellent ")

    elif score >= 50:
        print("Your grade is: Passable ")

    else:
        print("Your grade is: Bad ")
    score = int(score)
    print("*" * score)


def get_score():

    score = float(input("Enter score: "))
    return score


main()
