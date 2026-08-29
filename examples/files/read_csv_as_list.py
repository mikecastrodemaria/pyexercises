"""Reading a CSV into a list of lists.

Each row becomes a list, reached by position. Simple, but fragile:
insert a column in the file and every position shifts.
"""

import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SAMPLE = os.path.join(HERE, "sample_campaigns.csv")

rows = []
with open(SAMPLE, encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file, delimiter=";")
    header = next(reader)
    for row in reader:
        rows.append(row)

print("columns   :", header)
print("data rows :", len(rows))
print("first row :", rows[0])

# Reaching a value by position
print("name of the first campaign:", rows[0][0])
print("its impressions as text   :", rows[0][3])

# Everything read from a file is text. Convert what you compute with
impressions = int(rows[0][3])
clicks = int(rows[0][4])
print("its CTR:", f"{clicks / impressions * 100:.2f} %")

# What to remember
# 1. csv.reader gives you lists of TEXT
# 2. Position 0 is the first column
# 3. Reading by position breaks as soon as the file layout changes
