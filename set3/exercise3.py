"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def super_asker(low, high, message):
    while True:
        number = input(message)
        try:
            number = int(number)
            if low <= number <= high:
                print(f"Alright, so {number}?")
                return number
            else:
                print(f"That's not quite right.. try again.")
        except ValueError as ve:
            print("can't turn that into a number")


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    You can refactor a bit, you should refactor a bit! Don't put the code all
    inside this function, think about reusable chunks of code that you can call
    in several places.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nWelcome to the guessing game!")

    upperBound = super_asker(-5000, 5000, "Enter an upper bound: ")
    lowerBound = super_asker(-5000, upperBound, "Enter a lower bound: ")

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False
    while not guessed:
        guessedNumber = super_asker(lowerBound, upperBound, "Guess a number: ")
        print(f"You guessed {guessedNumber},")
        if guessedNumber == actualNumber:
            guessed = True
        elif guessedNumber < lowerBound or guessedNumber > upperBound:
            print(f"Error, guess is outside of range. Please try again.")
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")

    return "You got it!"
    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
