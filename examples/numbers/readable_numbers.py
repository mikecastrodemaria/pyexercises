"""Readable large numbers.

Two small tricks that make numbers easier for humans.
"""

# Underscores inside a number are ignored by Python
impressions = 1_765_000
print(impressions)

# Formatting with a thousands separator, for display only
print(f"{impressions:,}")
print(f"{impressions:,}".replace(",", " "))   # space separator

# Percentages
clicks = 59925
ctr = clicks / impressions
print("CTR as a ratio  :", ctr)
print("CTR as a percent:", f"{ctr * 100:.2f} %")

# What to remember
# 1. 1_765_000 and 1765000 are the same value
# 2. f"{value:,}" adds thousands separators for display
# 3. A rate becomes a percentage by multiplying by 100
