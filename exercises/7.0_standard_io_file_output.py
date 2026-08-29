"""Exercise 7.0 — Standard input and writing a CSV

Goal
    Collect information from the user and save it to a file.

In class
    Ask for a first name, a last name, an email and a student number,
    then write them to a CSV file.

Improved version
    Add the data to the file instead of replacing it, so several students
    can be recorded one after the other. Check the input before saving:
        the names must not be empty
        the email must contain an @
        the student number must be digits only
    Ask again when a value is not acceptable.

Expected file
    See 7.0_student_data.csv for the columns your file must have.

Hints
    open(path, "w") replaces the file, open(path, "a") adds to it.
    csv.writer() writes rows. Write the header only when the file is new.
    os.path.exists(path) tells you whether the file is already there.
    See ../examples/files/write_a_csv.py

Four steps
    Ask, read, adapt, check. Open the file afterwards and look at it.
"""

# TODO 1: collect the four values and write them to a CSV file


# TODO 2 (improved version): append instead of replace, and validate every value
