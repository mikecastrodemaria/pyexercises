"""Assignment operators."""

total = 0
print("start      :", total)

total = total + 10
print("total + 10 :", total)

# The short forms do the same thing
total += 5
print("total += 5 :", total)

total -= 3
print("total -= 3 :", total)

total *= 2
print("total *= 2 :", total)

total /= 4
print("total /= 4 :", total)

print("-" * 30)

# = assigns, == compares. This is the classic beginner trap
x = 5           # assignment
print("x == 5 ?", x == 5)   # comparison

print("-" * 30)

# Careful with lists: two names can point at the SAME list
first = [1, 2, 3]
second = first
second.append(4)
print("first :", first)     # it changed too
copy = first.copy()
copy.append(5)
print("first after copying:", first)

# What to remember
# 1. += is shorthand for "add to what is already there"
# 2. = assigns, == compares
# 3. Assigning a list does not copy it. Use .copy() when you need a real copy
