"""Defining and calling a function.

A function gives a name to a piece of work so you can run it whenever you want.
"""

def greet():
    """Prints a fixed greeting."""
    print("Hello, World!")

# Defining does nothing on its own. Calling runs it
greet()
greet()

print("-" * 30)

def greet_person(name):
    """Prints a greeting for the name it receives."""
    print("Hello,", name)

greet_person("Alice")
greet_person("Bob")

print("-" * 30)

def add(first, second):
    """Returns the sum of the two numbers it receives."""
    return first + second

result = add(2, 3)
print("2 + 3 =", result)
print("used directly:", add(10, 5) * 2)

print("-" * 30)

# A function without return gives back None
def shout(text):
    print(text.upper())

value = shout("careful")
print("what shout() returned:", value)

# What to remember
# 1. def defines, the parentheses call
# 2. return sends a value back, print only displays it
# 3. A function with no return gives back None
