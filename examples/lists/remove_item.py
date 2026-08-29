"""Removing items from a list.

Four ways, and they behave differently. Read the comments before choosing.
"""

channels = ["Meta Ads", "Google Ads", "LinkedIn Ads", "TikTok Ads", "Email"]
print("start   :", channels)

# remove() removes the first item equal to the value
channels.remove("Google Ads")
print("remove():", channels)

# pop() removes by position AND returns the item
removed = channels.pop(0)
print("pop(0)  :", channels, "| removed:", removed)

# pop() with no argument removes the last one
last = channels.pop()
print("pop()   :", channels, "| removed:", last)

# del removes by position, and returns nothing
del channels[0]
print("del     :", channels)

# clear() empties the list
channels.clear()
print("clear() :", channels)

# Removing a value that is not there stops the program
# channels.remove("Nothing")   # ValueError: list.remove(x): x not in list

# What to remember
# 1. remove() works on the value, pop() and del work on the position
# 2. pop() gives you back the item it removed
# 3. Never remove items from a list while looping over it, the positions shift
