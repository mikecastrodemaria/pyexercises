"""Reading a CSV into dictionaries.

Each row becomes a dictionary reached by column name. Safer than by position,
and much easier to read six months later. This is the version to prefer.
"""

import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SAMPLE = os.path.join(HERE, "sample_campaigns.csv")

campaigns = []
with open(SAMPLE, encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file, delimiter=";")
    for row in reader:
        campaigns.append(row)

print("rows read:", len(campaigns))
print("first row:", campaigns[0])

print("-" * 30)

for row in campaigns:
    # A missing or empty cell is an empty string, not a crash
    if not row["Impressions"].strip():
        print("skipping", row["Campaign"], "because impressions are missing")
        continue
    impressions = int(row["Impressions"])
    clicks = int(row["Clicks"])
    print(f"{row['Campaign']:<20} CTR {clicks / impressions * 100:.2f} %")

# What to remember
# 1. DictReader uses the first line as the column names
# 2. row["Campaign"] is clearer and safer than row[0]
# 3. An empty cell arrives as "", so test before converting
