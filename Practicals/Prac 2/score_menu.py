import random


def main():

    score = get_score()
    if score > 100:
        get_score()
    elif score < 0:
        get_score()
    print_grade(score)

    score = random_score()
    print("Random score:", score)
    print_grade(score)


def print_grade(score):
    if score >= 90:
        print("Excellent ")

    elif score >= 50:
        print("Passable ")

    else:
        print("Bad ")


def random_score():
    score = random.randint(0, 100)
    return score


def get_score():
    MENU = """Please input your score (between 0 and 100)"""
    print(MENU)
    score = float(input("Enter score: "))
    return score


main()
