"""Indexing and slicing a list.

A list is an ordered series of items. Positions start at 0, not 1.
"""

channels = ["Meta Ads", "Google Ads", "LinkedIn Ads", "TikTok Ads", "Email"]

print("the whole list :", channels)
print("how many items :", len(channels))

# Indexing: one item
print("first          :", channels[0])
print("second         :", channels[1])
print("last           :", channels[-1])     # negative counts from the end
print("second to last :", channels[-2])

# Slicing: a range of items. The end position is excluded
print("first three    :", channels[0:3])
print("same, shorter  :", channels[:3])
print("from the third :", channels[2:])
print("every other one:", channels[::2])
print("reversed       :", channels[::-1])

# Asking for a position that does not exist stops the program
# print(channels[99])   # IndexError: list index out of range

# What to remember
# 1. The first item is at position 0
# 2. In a slice the end position is excluded: [0:3] gives 3 items
# 3. -1 is the last item
