"""Displaying a list with a loop.

A for loop takes each item of the list in turn.
"""

names = ["Alice", "Bob", "Charlie", "David"]

# The simple form: the variable takes each value in turn
for name in names:
    print("Hello,", name)

print("-" * 30)

# With the position, using enumerate()
for position, name in enumerate(names):
    print(position, name)

print("-" * 30)

# Starting the count at 1, which is what a human expects
for number, name in enumerate(names, start=1):
    print(f"{number}. {name}")

print("-" * 30)

# Building a new list while looping
lengths = []
for name in names:
    lengths.append(len(name))
print("name lengths:", lengths)

# What to remember
# 1. for <variable> in <list>: takes each item in turn
# 2. The indented block is what gets repeated
# 3. enumerate() gives you the position as well as the item
