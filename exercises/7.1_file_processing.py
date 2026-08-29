"""Exercise 7.1 — Reading and processing a file

Goal
    Read a file, clean what is inside, and write the result somewhere else.
    This is the direct rehearsal for the final project.

In class
    Read names.txt, display every name it contains.

Improved version
    Read names.txt, then:
        remove the spaces and line breaks around each name
        capitalise them properly, so "ada LOVELACE" becomes "Ada Lovelace"
        sort them by LAST name, not by first name
        write the result to sorted_names.txt
    Ignore empty lines instead of crashing on them.

Hints
    with open(path) as file: opens and closes the file for you.
    .readlines() gives a list of lines, each ending with \\n.
    .strip() removes it. .title() fixes the capitals. .split() separates the words.
    sorted(names, key=...) sorts on something other than the whole string.
    See ../examples/files/read_a_csv.py for the opening pattern.

Four steps
    Ask, read, adapt, check. Open sorted_names.txt and verify the order yourself.
"""

# TODO 1: read names.txt and display every name


# TODO 2 (improved version): clean, sort by last name, and write the result to a file
