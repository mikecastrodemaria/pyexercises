"""Adding, updating and removing in a dictionary."""

campaign = {"name": "Winter Sale", "clicks": 4838}
print("start      :", campaign)

# Adding a key: just assign it
campaign["cost"] = 11088.60
print("added      :", campaign)

# Updating: same syntax, existing key
campaign["clicks"] = 5000
print("updated    :", campaign)

# update() adds or updates several at once
campaign.update({"channel": "Meta Ads", "conversions": 290})
print("update()   :", campaign)

# pop() removes a key and returns its value
cost = campaign.pop("cost")
print("pop('cost'):", campaign, "| removed:", cost)

# A dictionary of dictionaries, which is how you will hold several campaigns
campaigns = {
    "Winter Sale": {"clicks": 4838, "conversions": 290},
    "Aurora Launch": {"clicks": 20221, "conversions": 824},
}
for name, data in campaigns.items():
    print(f"{name}: {data['conversions']} conversions")

# What to remember
# 1. Assigning to a new key creates it, no special method needed
# 2. pop() removes and gives you the value back
# 3. Dictionaries inside dictionaries are normal and very useful
