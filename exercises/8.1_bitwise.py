"""Exercise 8.1 — Bitwise operators (bonus, not graded)

Goal
    Understand how permissions are stored as bits, the way Linux and macOS do it.

Task
    Define READ, WRITE and EXECUTE as 4, 2 and 1. Combine read and write into
    one value. Test whether that value includes execute. Then add execute,
    and remove write.

Improved version
    Write a function that turns a permission value into a readable string,
    such as "rw-" or "r-x".

Hints
    | adds a flag, & tests one, ~ inverts. bin(value) shows the bits.
    See ../examples/operators/bitwise.py

Four steps
    Ask, read, adapt, check.
"""

# TODO: combine, test, add and remove permissions
