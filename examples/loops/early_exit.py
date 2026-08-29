"""Leaving a loop early, and skipping one turn."""

names = ["Alice", "Bob", "Charlie", "David"]

# break stops the loop completely
for name in names:
    print("checking", name)
    if name == "Charlie":
        print("found Charlie, stopping")
        break

print("-" * 30)

# continue skips the rest of this turn and goes to the next item
for name in names:
    if name.startswith("B"):
        continue
    print("kept:", name)

print("-" * 30)

# Searching, the readable way
target = "David"
found = False
for name in names:
    if name == target:
        found = True
        break
print(target, "found?", found)

print("-" * 30)

# Skipping rows that cannot be used, the pattern of the final project
rows = [{"name": "A", "impressions": 1000}, {"name": "B", "impressions": None}]
for row in rows:
    if not row["impressions"]:
        print("skipping", row["name"], "because impressions are missing")
        continue
    print("using", row["name"])

# What to remember
# 1. break leaves the loop, continue skips to the next turn
# 2. continue is how you ignore a bad row without crashing
# 3. A flag variable like found is clearer than a clever trick
