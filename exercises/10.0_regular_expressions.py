"""Exercise 10.0 — Regular expressions (bonus, not graded)

Goal
    Check the shape of a piece of text: is this really an email address?

Task
    Search for a word inside a sentence using the re module, and say whether
    it was found.

Improved version
    Write three validation functions:
        a name contains only letters and spaces
        an email looks like something@something.something
        a student number is exactly eight digits
    Ask the user for the three values, validate each one, and only save them
    to a CSV file when all three are acceptable.

Hints
    import re, then re.search(pattern, text) or re.match(pattern, text).
    A pattern is a small language of its own. Ask the AI to explain the
    pattern it gives you, line by line, before you use it.

Four steps
    Ask, read, adapt, check. Test with a deliberately wrong email.
"""

# TODO: search for a word, then validate three kinds of value
