"""Exercise 9.0 — Handling errors

Goal
    Keep the program alive when something goes wrong. You will need this
    in the final project, where two campaigns have zero conversions.

Task
    Ask the user for a number and display it. If the user types something
    that is not a number, say so instead of crashing.

Improved version
    Also divide 10 by that number, and handle two different problems
    separately:
        ValueError, when the text is not a number
        ZeroDivisionError, when the number is zero
    Then keep asking until the user gives an acceptable value.

Hints
    try: the risky code
    except ValueError: what to do in that case
    except ZeroDivisionError: what to do in that other case
    Catching the specific error is better than catching everything.

Four steps
    Ask, read, adapt, check. Test with "abc", with 0, and with 5.
"""

# TODO 1: read a number, and survive a wrong entry


# TODO 2 (improved version): divide, handle both errors, keep asking until it works
