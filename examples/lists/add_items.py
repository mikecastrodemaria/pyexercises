"""Adding items to a list."""

fruits = ["apple", "banana"]
print("start        :", fruits)

# append() adds one item at the end
fruits.append("cherry")
print("append()     :", fruits)

# insert() adds at a chosen position
fruits.insert(0, "avocado")
print("insert(0, ..):", fruits)

# extend() adds every item of another list
fruits.extend(["dates", "elderberry"])
print("extend()     :", fruits)

# + creates a NEW list instead of modifying this one
more = fruits + ["fig"]
print("with +       :", more)
print("original     :", fruits)

# A list can hold anything, even mixed types
mixed = [1, "two", 3.0, True]
print("mixed list   :", mixed)

# What to remember
# 1. append() adds one item, extend() adds several
# 2. append() modifies the list in place and returns nothing
# 3. + builds a new list and leaves the original alone
