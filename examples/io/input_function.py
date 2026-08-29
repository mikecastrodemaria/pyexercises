"""Reading what the user types, with input().

input() stops the program and waits. Whatever the user types comes back as TEXT.
"""

# Run this file and answer in the terminal at the bottom of your editor.
name = input("What is your name? ")
print("Hello,", name)

# input() always returns text, even when the user types digits
age_text = input("How old are you? ")
print("what we received:", repr(age_text), "of type", type(age_text))

# Convert before computing
age = int(age_text)
print("next year you will be", age + 1)

# Cleaning the input is almost always worth it
answer = input("Continue? (yes/no) ").strip().lower()
print("cleaned answer:", repr(answer))

if answer == "yes":
    print("Off we go.")
else:
    print("Stopping here.")

# What to remember
# 1. input() always gives text, never a number
# 2. int() and float() convert, and crash if the text is not a number
# 3. .strip().lower() removes the spaces and the capitals before you compare
