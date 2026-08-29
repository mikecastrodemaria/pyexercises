"""Comparison operators. Each one answers True or False."""

a = 10
b = 3

print("a == b :", a == b)   # equal
print("a != b :", a != b)   # not equal
print("a > b  :", a > b)
print("a < b  :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

print("-" * 30)

# Comparisons work on text too, in alphabetical order
print("'apple' < 'banana' :", "apple" < "banana")
print("'Apple' == 'apple' :", "Apple" == "apple")     # capitals matter
print("case-insensitive   :", "Apple".lower() == "apple".lower())

print("-" * 30)

# This is exactly how you check a quiz answer
correct = "Aurora Launch"
given = "  aurora launch  "
print("naive comparison  :", given == correct)
print("cleaned comparison:", given.strip().lower() == correct.lower())

print("-" * 30)

# Python allows chained comparisons
score = 4
print("between 1 and 5 ?", 1 <= score <= 5)

# What to remember
# 1. A comparison produces True or False, nothing else
# 2. Text comparison is case sensitive. Clean both sides before comparing
# 3. strip() and lower() on user input save you many wrong answers
