"""Logical operators: and, or, not."""

x = True
y = False

print("x and y :", x and y)   # True only if both are true
print("x or y  :", x or y)    # True if at least one is true
print("not x   :", not x)

print("-" * 30)

# Combining real tests
impressions = 283000
conversions = 0
cost = 11088.60

if impressions > 0 and conversions > 0:
    print("we can compute a CPA")
else:
    print("no CPA possible for this campaign")

if conversions == 0 or cost == 0:
    print("at least one value is zero, watch out for divisions")

print("-" * 30)

# Python treats some values as false: 0, "", [], {}, None
values = [0, "", [], {}, None, 1, "text", [1]]
for value in values:
    print(repr(value), "is treated as", bool(value))

# Which lets you write this
name = ""
if not name:
    print("the name is empty")

# What to remember
# 1. and needs both sides, or needs one
# 2. Empty values (0, "", [], None) count as false
# 3. "if not value" is the usual way to test for empty or missing
