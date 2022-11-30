"""
CP1404 Prac 10 - Testing
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def phrase_as_sentence(phrase):
    sentence = phrase.capitalize()
    if sentence[-1] != ".":
        sentence += "."
    return sentence


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # set fuel using fuel = 10 (passing value in)
    test_car = Car(fuel=10)
    assert test_car.fuel == 10

    # set fuel using default
    test_car_2 = Car()
    assert test_car_2.fuel == 0

    # Test 1 'hello' -> 'Hello.'
    test_phrase = "hello"
    test_sentence = phrase_as_sentence(test_phrase)
    assert test_sentence == "Hello."

    # Test 2 'It is an ex parrot.' -> 'It is an ex parrot.'
    test_phrase_2 = 'It is an ex parrot.'
    test_sentence_2 = phrase_as_sentence(test_phrase_2)
    assert test_sentence_2 == 'It is an ex parrot.'

    # Test 3 "final Test, here" -> "Final test, here."
    test_phrase_3 = "final Test, here"
    test_sentence_3 = phrase_as_sentence(test_phrase_3)
    assert test_sentence_3 == "Final test, here."


run_tests()


doctest.testmod()

