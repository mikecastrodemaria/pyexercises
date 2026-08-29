"""Counted loops.

A for loop repeats once per item, or once per number in a range.
"""

# Over a range of numbers. range(5) gives 0, 1, 2, 3, 4
for i in range(5):
    print("iteration", i + 1)

print("-" * 30)

# range(start, stop) excludes the stop value
for number in range(1, 6):
    print(number, "squared is", number ** 2)

print("-" * 30)

# range(start, stop, step)
for number in range(0, 20, 5):
    print(number)

print("-" * 30)

# Over a list, which is what you will do most often
questions = ["Best CTR?", "Highest CPA?", "How many above ROAS 3?"]
for question in questions:
    print("Question:", question)

print("-" * 30)

# Accumulating a total while looping
conversions = [290, 824, 4125, 0]
total = 0
for value in conversions:
    total = total + value
print("total conversions:", total)

# What to remember
# 1. range(n) starts at 0 and stops before n
# 2. Looping over a list is more readable than looping over positions
# 3. The accumulator pattern (total = total + value) is how you build a score
