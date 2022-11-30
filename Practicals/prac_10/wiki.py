"""
CP1404 Prac 10 - Wikipedia API & Python Library
Testing demo using assert and doctest
"""
import wikipedia

userinput = input("Enter title page or search phrase.\n>>> ")

while userinput != "":
    try:
        page_data = wikipedia.page(userinput)
        print(page_data.title)
        print(page_data.summary)
        print(page_data.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"The top three results are:\n{e.options[1]}, {e.options[2]}, {e.options[3]}")
    except wikipedia.exceptions.PageError:
        print(f"{userinput} does not exist. Try another search")
    print()
    userinput = input("Enter title page or search phrase.\n>>> ")
