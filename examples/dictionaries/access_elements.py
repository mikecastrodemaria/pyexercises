"""Reading a dictionary.

A dictionary stores values you reach by name (the key) instead of by position.
"""

campaign = {
    "name": "Winter Sale",
    "channel": "Meta Ads",
    "impressions": 283000,
    "clicks": 4838,
}

print("the whole thing:", campaign)

# Reading with square brackets
print("name           :", campaign["name"])
print("clicks         :", campaign["clicks"])

# A missing key stops the program
# print(campaign["cost"])   # KeyError: 'cost'

# get() returns None instead of stopping, or a default value you choose
print("get('cost')    :", campaign.get("cost"))
print("get with default:", campaign.get("cost", 0))

# Testing before reading
if "clicks" in campaign:
    print("clicks are there")

# Looping over a dictionary
for key in campaign:
    print(" key:", key)

for key, value in campaign.items():
    print(f" {key} = {value}")

print("keys           :", list(campaign.keys()))
print("values         :", list(campaign.values()))

# What to remember
# 1. campaign["name"] stops the program if the key is missing
# 2. campaign.get("name", default) never stops
# 3. .items() gives you the key and the value together
