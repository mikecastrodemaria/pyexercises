"""The list methods you will actually use."""

numbers = [5, 2, 8, 1, 3]
print("start          :", numbers)

# sort() reorders the list itself and returns nothing
numbers.sort()
print("sort()         :", numbers)

numbers.sort(reverse=True)
print("sort(reverse)  :", numbers)

# sorted() returns a NEW sorted list and leaves the original alone
words = ["banana", "apple", "cherry"]
print("sorted()       :", sorted(words), "| original:", words)

# reverse() flips the order
numbers.reverse()
print("reverse()      :", numbers)

# Useful built-in functions
print("len()          :", len(numbers))
print("min() max()    :", min(numbers), max(numbers))
print("sum()          :", sum(numbers))
print("average        :", sum(numbers) / len(numbers))

# count() and index()
letters = ["a", "b", "a", "c"]
print("count('a')     :", letters.count("a"))
print("index('b')     :", letters.index("b"))

# in tests membership
print("'c' in letters :", "c" in letters)

# What to remember
# 1. sort() changes the list, sorted() gives a new one
# 2. sum(), min(), max(), len() cover most calculations
# 3. "value in list" is the quickest way to test membership
