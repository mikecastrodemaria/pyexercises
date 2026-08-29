"""Creating a dictionary.

A list finds things by position. A dictionary finds them by name.
When your data has named fields, a dictionary is the right shape.
"""

# Curly brackets, and key: value pairs
campaign = {
    "name": "Winter Sale",
    "channel": "Meta Ads",
    "impressions": 283000,
    "clicks": 4838,
}
print("campaign :", campaign)
print("length   :", len(campaign))

# An empty dictionary, to fill later
totals = {}
totals["Email"] = 0
totals["Meta Ads"] = 290
print("built up :", totals)

# Keys are usually text, values can be anything
student = {
    "name": "Alice",
    "age": 22,
    "scores": [4, 5, 3],
    "active": True,
}
print("student  :", student)
print("scores   :", student["scores"])

# Same information as a list, and why that is worse
as_list = ["Winter Sale", "Meta Ads", 283000, 4838]
print("as a list:", as_list)
print("position 2 is impressions... if nobody ever inserts a column")
print("by name  :", campaign["impressions"], "reads better and does not move")

# Building a dictionary from two lists
keys = ["name", "channel"]
values = ["Aurora Launch", "Google Ads"]
print("zipped   :", dict(zip(keys, values)))

# What to remember
# 1. {} creates a dictionary, keys are names you choose
# 2. Reading by name survives a change of file layout, reading by position does not
# 3. A dictionary is the natural shape for one row of a CSV file
