"""
CP1404 Prac 9 - Taxi simulator

"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

menu = """(Q)uit
(C)hoose taxi
(D)rive"""


def main():
    """"""
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_bill = 0
    print("let's drive!")
    menu_choice = input(f"{menu}\n>>> ").upper()

    while menu_choice != "Q":
        if menu_choice == "C":
            print("Taxis available: ")
            display_taxis(taxis)
        elif menu_choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                print()

        else:
            print("Invalid choice")

        menu_choice = input(f"{menu}\n>>> ").upper


def display_taxis(taxis):
    for taxi_number, taxi in enumerate(taxis):
        print(taxi)


main()
