"""Removing entries from a dictionary."""

campaign = {
    "name": "Winter Sale",
    "channel": "Meta Ads",
    "impressions": 283000,
    "clicks": 4838,
    "draft_note": "to be deleted",
}
print("start        :", campaign)

# pop() removes a key and gives you back its value
note = campaign.pop("draft_note")
print("pop()        :", campaign, "| removed:", note)

# pop() with a default never crashes, even if the key is absent
missing = campaign.pop("cost", None)
print("pop absent   :", missing)

# Without a default, a missing key stops the program
# campaign.pop("cost")   # KeyError: 'cost'

# del removes, and returns nothing
del campaign["clicks"]
print("del          :", campaign)

# popitem() removes the last inserted pair
last = campaign.popitem()
print("popitem()    :", campaign, "| removed:", last)

# clear() empties it
campaign.clear()
print("clear()      :", campaign)

# Removing while looping breaks the loop. Build the list of keys first
scores = {"Alice": 4, "Bob": 0, "Charlie": 5, "Dana": 0}
to_remove = [name for name, score in scores.items() if score == 0]
for name in to_remove:
    del scores[name]
print("cleaned      :", scores)

# What to remember
# 1. pop(key, default) is the safe form, it never crashes
# 2. del removes but gives nothing back
# 3. Never delete from a dictionary while looping over it. List the keys first
