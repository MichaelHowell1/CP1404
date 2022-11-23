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
            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi choice")

        elif menu_choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                drive_distance = float(input("Drive how far? "))
                current_taxi.drive(drive_distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost}")
                total_bill += trip_cost
        else:
            print("Invalid choice")

        print(f"Bill to date ${total_bill}")
        menu_choice = input(f"{menu}\n>>> ").upper()


def display_taxis(taxis):
    for taxi_number, taxi in enumerate(taxis):
        print(f"{taxi_number} - {taxi}")


main()
