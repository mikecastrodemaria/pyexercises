"""Creating a list.

A list holds several values in one place, in the order you put them.
"""

# The usual way: square brackets
fruits = ["apple", "banana", "cherry"]
print("fruits     :", fruits)

# An empty list, to fill later
scores = []
print("empty      :", scores, "| length:", len(scores))

# Another way, rarely used but you will see it
also_empty = list()
print("list()     :", also_empty)

# A list can hold anything, including other lists
mixed = [1, "two", 3.0, True]
nested = [["Winter Sale", 4838], ["Aurora Launch", 20221]]
print("mixed      :", mixed)
print("nested     :", nested)
print("inside     :", nested[0][0], "had", nested[0][1], "clicks")

# Building a list from text, which is what reading a file gives you
line = "Meta Ads;Google Ads;LinkedIn Ads"
channels = line.split(";")
print("from text  :", channels)

# Repeating a value, useful to prepare a list of a known size
zeros = [0] * 5
print("five zeros :", zeros)

# What to remember
# 1. [] creates a list, len() counts it
# 2. The order you put things in is the order you get them back
# 3. split() turns a line of text into a list
