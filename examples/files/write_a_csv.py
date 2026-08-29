"""Writing a CSV file.

The mirror image of reading. This is how the final project saves its result.
"""

import csv
import os
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(HERE, "example_result.csv")

results = [
    {"player": "Alice", "score": 4, "date": str(date.today())},
    {"player": "Bob", "score": 2, "date": str(date.today())},
]

# "w" replaces the file. "a" adds at the end without erasing
with open(OUTPUT, "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["player", "score", "date"], delimiter=";")
    writer.writeheader()
    for row in results:
        writer.writerow(row)

print("written:", OUTPUT)

# Reading it back is the quickest way to check you wrote what you meant
with open(OUTPUT, encoding="utf-8-sig", newline="") as file:
    print(file.read())

# What to remember
# 1. "w" erases the file, "a" appends to it
# 2. writeheader() writes the column names once
# 3. Always read the file back once, to check
