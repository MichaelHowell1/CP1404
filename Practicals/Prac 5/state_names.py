"""
CP1404 Prac 5 - State Name
Check abbreviation against matching state names and display
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        state_code in CODE_TO_NAME
        print(f"{state_code:3} is {CODE_TO_NAME[state_code]}")
        state_code = ""
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
