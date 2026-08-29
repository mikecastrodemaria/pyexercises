"""Slicing a list.

Indexing gives you one item. Slicing gives you a range of them,
and always returns a NEW list.
"""

channels = ["Meta Ads", "Google Ads", "LinkedIn Ads", "TikTok Ads", "Email", "Display"]
print("full list      :", channels)

# [start:end] — the end position is EXCLUDED
print("[0:3]          :", channels[0:3])
print("[2:5]          :", channels[2:5])

# Leaving a side out means "from the beginning" or "to the end"
print("[:3]           :", channels[:3])
print("[3:]           :", channels[3:])
print("[:]            :", channels[:])       # a full copy

# Negative positions count from the end
print("[-2:]          :", channels[-2:])     # the last two
print("[:-2]          :", channels[:-2])     # everything but the last two

# A third number is the step
print("[::2]          :", channels[::2])     # every other one
print("[::-1]         :", channels[::-1])    # reversed

# Slicing never crashes, even out of range
print("[10:20]        :", channels[10:20])   # empty list, no error
# channels[10] would crash. Slicing does not.

# The original is untouched
print("still original :", channels)

# Slicing works on strings too
word = "Programming"
print("word[0:7]      :", word[0:7])
print("word[-4:]      :", word[-4:])

# What to remember
# 1. The end position is excluded: [0:3] gives three items
# 2. A slice returns a new list, the original does not move
# 3. [::-1] reverses, and it works on strings as well
