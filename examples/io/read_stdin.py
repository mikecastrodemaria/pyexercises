"""Reading standard input with sys.stdin.

Standard input is the stream a program reads from. input() uses it under the hood.
This file shows the lower-level version, which is useful when data is piped in.
"""

import sys

print("Type a few lines, then press Ctrl+D (Ctrl+Z on Windows) to finish.")

lines = sys.stdin.readlines()

print("-" * 30)
print("lines received:", len(lines))
for position, line in enumerate(lines, start=1):
    print(position, repr(line))       # note the \n at the end of each line

# strip() removes that line break
cleaned = [line.strip() for line in lines]
print("cleaned:", cleaned)

# In a terminal you could also run:
#   echo "hello" | python3 read_stdin.py

# What to remember
# 1. sys.stdin.readlines() reads everything at once, into a list
# 2. Every line keeps its \n until you strip() it
# 3. For a course exercise, input() is almost always enough
