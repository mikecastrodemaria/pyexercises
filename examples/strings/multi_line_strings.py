"""Multi-line strings.

Three quotes in a row open a string that can span several lines.
Useful for long text, and for the documentation block at the top of a file.
"""

# Triple double quotes
address = """SKEMA Business School
60 rue Dostoievski
06902 Sophia Antipolis"""

print(address)
print("-" * 30)

# Triple single quotes work the same way
menu = '''1. Start the quiz
2. See the scores
3. Quit'''

print(menu)
print("-" * 30)

# The line breaks are really inside the string
print("Number of characters:", len(address))
print("Number of lines:", len(address.split("\n")))

# A single-line string can also contain a line break, written \n
compact = "Line one\nLine two"
print(compact)

# What to remember
# 1. Triple quotes keep the layout you typed
# 2. \n is a line break inside a normal string
# 3. The block at the top of this file is a multi-line string. Python uses it as documentation
