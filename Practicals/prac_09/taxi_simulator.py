"""
CP1404 Prac 9 - Taxi simulator
A simulator for a taxi trip using different cars and drive distances
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

menu = """(Q)uit
(C)hoose taxi
(D)rive"""


def main():
    """From list choose a taxi and drive specified distance.
    According to price_per_km calculation the cost of the trip is calculated then added to the total bill.
    The trip continues until user selects quit option which displays all car information and total bill."""

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
            except ValueError:
                print("Invalid taxi choice")

        elif menu_choice == "D":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                try:
                    drive_distance = float(input("Drive how far? "))
                    current_taxi.drive(drive_distance)
                    trip_cost = current_taxi.get_fare()
                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                    total_bill += trip_cost
                except ValueError:
                    print("Invalid taxi choice")
        else:
            print("Invalid choice")

        print(f"Bill to date ${total_bill:.2f}")
        menu_choice = input(f"{menu}\n>>> ").upper()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display taxi information alongside its number"""
    for taxi_number, taxi in enumerate(taxis):
        print(f"{taxi_number} - {taxi}")


main()
