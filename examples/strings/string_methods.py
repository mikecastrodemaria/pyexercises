"""Common string methods.

A method is an action attached to a value. You call it with a dot.
Strings never change: every method returns a NEW string.
"""

text = "  Campaign Audit Quiz  "

print("original      :", repr(text))
print("strip()       :", repr(text.strip()))        # removes spaces at both ends
print("upper()       :", text.strip().upper())
print("lower()       :", text.strip().lower())
print("title()       :", "mike castro".title())     # capitalises each word
print("replace()     :", text.strip().replace(" ", "_"))
print("startswith()  :", text.strip().startswith("Campaign"))
print("find()        :", text.strip().find("Audit"))   # position, or -1 if absent

# split() cuts a string into a list, join() puts a list back together
line = "Winter Sale;Meta Ads;283000"
fields = line.split(";")
print("split(';')    :", fields)
print("join()        :", " | ".join(fields))

# The original is untouched
print("still original:", repr(text))

# Numbers arriving as text must be converted before you can compute with them
value_as_text = "283000"
value_as_number = int(value_as_text)
print(value_as_number + 1)

# What to remember
# 1. Methods return a new string, they never modify the original
# 2. split() and join() are the two you will use most with files
# 3. Text that looks like a number is still text until you convert it
