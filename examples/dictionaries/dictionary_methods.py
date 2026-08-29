"""Dictionary methods, and turning a list into a dictionary."""

scores = {"Alice": 4, "Bob": 2, "Charlie": 5}

print("keys    :", list(scores.keys()))
print("values  :", list(scores.values()))
print("items   :", list(scores.items()))
print("length  :", len(scores))

# Finding the highest value, and the key that carries it
print("best score :", max(scores.values()))
print("best player:", max(scores, key=scores.get))

# Sorting by value, highest first
ranking = sorted(scores.items(), key=lambda pair: pair[1], reverse=True)
for position, (player, score) in enumerate(ranking, start=1):
    print(f"{position}. {player}: {score}")

# Counting with a dictionary: the pattern you will reuse in the final project
channels = ["Email", "Meta Ads", "Email", "Google Ads", "Email"]
count = {}
for channel in channels:
    count[channel] = count.get(channel, 0) + 1
print("count per channel:", count)

# What to remember
# 1. max(d, key=d.get) gives the key holding the largest value
# 2. d.get(key, 0) + 1 is the standard way to count things
# 3. sorted(d.items(), key=...) builds a ranking
