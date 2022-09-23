
"""CP1404 Prac 1 Michael Howell"""

name = input("What is your name?")
menu = """Please pick one of the following options
(H)ello
(G)oodbye
(Q)uit"""
print(menu)
choice = input (" ").upper()
while choice != "Q":
    if choice == "H":
        print ("Hello", name)
    elif choice == "G":
        print ("Goodbye", name)
    else:
        print ("Please choose a valid option")
    print()
    print (menu)
    """reasks question and converts all answers to uppercase to allow for both upper and lower case responses"""
    choice = input(" ").upper()
print ("Process complete.")