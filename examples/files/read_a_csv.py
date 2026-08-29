"""Reading a CSV file.

CSV means Comma Separated Values, except in Europe where spreadsheets
usually write semicolons and decimal commas. Read the file, do not assume.
"""

import csv
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SAMPLE = os.path.join(HERE, "sample_campaigns.csv")

# encoding="utf-8-sig" removes the invisible marker a spreadsheet puts first.
# newline="" is what the csv module expects.
with open(SAMPLE, encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        print(row)

print("-" * 30)

# Skipping the header line
with open(SAMPLE, encoding="utf-8-sig", newline="") as file:
    reader = csv.reader(file, delimiter=";")
    header = next(reader)
    print("columns:", header)
    for row in reader:
        print(row[0], "->", row[3], "impressions")

# What to remember
# 1. Open with encoding="utf-8-sig" and newline=""
# 2. Say which delimiter the file really uses
# 3. next(reader) reads the header line and moves past it
