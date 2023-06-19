# -*- coding: UTF-8 -*-
"""Set 3.

Modify each function until the tests pass.
"""


def loop_ranger(start, stop=None, step=2):
    """Return a list of numbers between start and stop in steps of step.

    Using a while loop make a list of numbers that goes from the start number up
    to, but not including, the stop number, in increments of step. E.g.:
        start: 3
        stop: 10
        step: 2
        will return: [3, 5, 7, 9]
    Look up for how range() works in the python docs. You could  answer this
    with just the range function, but we'd like you to do it the long way.
    """

    ranger = []

    while start < stop:
        ranger.append(start)
        start += step
    return ranger


def two_step_ranger(start, stop):
    """Make a range that steps by 2.

    Sometimes you want to hide complexity.
    Make a range function that always has a step size of 2

    You can either reuse loop_ranger, or the range function that in the standard library
    """

    my_range = []
    for i in range(start, stop, 2):
        my_range.append(i)
    return my_range


def stubborn_asker(low, high):
    """Ask for a number between low and high until actually given one.

    Ask for a number, and if the response is outside the bounds keep asking
    until you get a number that you think is OK

    Look up the docs for a function called "input"
    """

    while True:
        number = int(input(f"Enter a number between {low} and {high} "))
        print(type(number), number, type(high), high, type(low), low)
        if (
            all([type(number) is int, type(high) is int, type(low) is int])
            and low <= number <= high
        ):
            print("You got it!")
            return "You got it!"
        else:
            print(
                "Are you dumb? Try again but better this time...",
                type(number),
                type(high),
                type(low),
            )


def not_number_rejector(message):
    """Ask for a number repeatedly until actually given one.

    Ask for a number, and if the response is actually NOT a number
    (e.g. "cow", "six", "8!") then throw it out and ask for an actual number.
    When you do get a number, return it.
    """

    real_number = False

    while not real_number:
        message = input(message)
        try:
            if message.isdigit():
                print(f"Cool, you know what a number is")
                real_number = True
            else:
                raise ValueError()
        except ValueError:
            print(f"That aint a damn number, try again: ")
            break
    return "You got it!"


def super_asker(low, high):
    """Robust asking function.

    Combine what you learnt from stubborn_asker and not_number_rejector
    to make a function that does it all!
    """
    in_range = False

    while not in_range:
        number = input(f"Enter a number between {low} and {high}: ")
        try:
            if number.isdigit():
                number = int(number)
            else:
                raise ValueError()
            if low <= number <= high:
                print(f"You got it!")
                in_range = True
            else:
                raise ValueError()
        except:
            ValueError
            print(f"That's not quite right.. try again.")
            break

    return "You got it!"


if __name__ == "__main__":
    # this section does a quick test on your results and prints them nicely.
    # It's NOT the official tests, they are in tests.py as usual.
    # Add to these tests, give them arguments etc. to make sure that your
    # code is robust to the situations that you'll see in action.
    # NOTE: because some of these take user input you can't run them from

    print("\nloop_ranger", loop_ranger(1, 10, 2))
    print("\ntwo_step_ranger", two_step_ranger(1, 10))
    print("\nstubborn_asker")
    stubborn_asker(30, 45)
    print("\nnot_number_rejector")
    not_number_rejector("Enter a number: ")
    print("\nsuper_asker")
    super_asker(33, 42)
