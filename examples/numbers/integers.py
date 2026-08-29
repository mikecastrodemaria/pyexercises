"""Integers.

Whole numbers, positive or negative. Python calls this type int.
"""

clicks = 4838
conversions = 290

print("clicks       :", clicks)
print("type         :", type(clicks))

# The usual arithmetic
print("addition     :", clicks + conversions)
print("subtraction  :", clicks - conversions)
print("multiplication:", conversions * 2)
print("division     :", clicks / conversions)      # always gives a float
print("floor division:", clicks // conversions)    # whole part only
print("remainder    :", clicks % conversions)      # what is left over
print("power        :", 2 ** 10)

# Python integers have no size limit
big = 9 ** 40
print("a very big integer:", big)

# The remainder is how you test whether a number is even
number = 7
print(number, "is even?", number % 2 == 0)

# What to remember
# 1. / always produces a float, even when the division is exact
# 2. // keeps only the whole part
# 3. % gives the remainder, and answers "is it a multiple of"
