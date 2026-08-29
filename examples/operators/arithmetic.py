"""Arithmetic operators."""

a = 17
b = 5

print("a + b  :", a + b)
print("a - b  :", a - b)
print("a * b  :", a * b)
print("a / b  :", a / b)      # float division
print("a // b :", a // b)     # whole part
print("a % b  :", a % b)      # remainder
print("a ** b :", a ** b)     # power

print("-" * 30)

# Priority is the usual mathematical one. Brackets remove all doubt
print("2 + 3 * 4    :", 2 + 3 * 4)
print("(2 + 3) * 4  :", (2 + 3) * 4)

print("-" * 30)

# The operators also work on text and lists, differently
print("'ab' * 3   :", "ab" * 3)
print("[1,2] + [3]:", [1, 2] + [3])

# What to remember
# 1. / gives a float, // gives the whole part
# 2. Use brackets rather than trusting your memory of priorities
# 3. + and * mean something else on strings and lists
