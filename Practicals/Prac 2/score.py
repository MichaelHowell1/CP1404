def main():

    score = get_score()

    while score != "Q":

        if score > 100:
            print("Please input a number between 0 and 100")
        elif score >= 90:
            print("Excellent ")
        elif score >= 50:
            print("Passable ")
        elif score >= 0:
            print("Bad ")

        else:
            print("Please input a number between 0 and 100")
        score = float(input("Enter score: "))


def get_score():
    MENU = """Please input your score (between 0 and 100)"""
    print(MENU)
    score = float(input("Enter score: "))
    return score



main()
