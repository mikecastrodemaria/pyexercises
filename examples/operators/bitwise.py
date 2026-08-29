"""Bitwise operators.

Bonus material, not covered in class. Here for the curious.
Bits are the ones and zeros a computer really works with.
"""

READ = 0b100     # 4
WRITE = 0b010    # 2
EXECUTE = 0b001  # 1

print("READ    :", READ, "in binary", bin(READ))
print("WRITE   :", WRITE, "in binary", bin(WRITE))
print("EXECUTE :", EXECUTE, "in binary", bin(EXECUTE))

# Combining permissions with OR
permissions = READ | WRITE
print("read + write :", permissions, bin(permissions))

# Testing a permission with AND
print("can read?    :", permissions & READ != 0)
print("can execute? :", permissions & EXECUTE != 0)

# Adding one
permissions = permissions | EXECUTE
print("after adding execute:", bin(permissions))

# Removing one
permissions = permissions & ~WRITE
print("after removing write:", bin(permissions))

# What to remember
# 1. | adds a flag, & tests one, ~ inverts
# 2. This is how file permissions work on Linux and macOS
# 3. You will not need this for the final project
