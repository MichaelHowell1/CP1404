"""
CP1404 Prac 5 - Hex Colours
Display hexadecimal codes for corresponding colour
"""
colour_to_code = {"absolute zero": "#0048ba", "acid green": "#b0bf1a", "aliceblue": "#f0f8ff",
                  "alizarin crimson": "#e32636", "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc",
                  "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc"}

colour_name = input("Enter a colour name or press enter to quit."
                    "\n>>> ").lower()
while colour_name != "":
    try:
        colour_name in colour_to_code
        print(f"The code for {colour_name:3} is {colour_to_code[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter a colour name or press enter to quit."
                        "\n>>> ").lower()
