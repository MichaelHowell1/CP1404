"""
CP1404 Prac 9 - Taxi simulator

"""

from prac_09.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

menu = """(Q)uit
(C)hoose taxi
(D)rive"""


def main():
    menu_choice = input(f"{menu}\n>>> ").upper
    while menu_choice != "Q":
        if menu_choice == "C":

        elif menu_choice == "D":

        else:
            print("Invalid choice")
    menu_choice = input(f"{menu}\n>>> ").upper



main()
