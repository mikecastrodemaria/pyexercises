"""Normal string literals.

A string is text. In Python you write it between single or double quotes.
Both work exactly the same way. Pick one style and stay consistent.
"""

# Single quotes and double quotes produce the same string
with_single = 'Hello'
with_double = "Hello"

print(with_single)
print(with_double)
print("Are they the same value?", with_single == with_double)

# Choose the quote that avoids escaping
sentence_with_apostrophe = "It's a good day"      # double quotes, no escaping needed
sentence_with_quotes = 'She said "hello" to me'   # single quotes, no escaping needed

print(sentence_with_apostrophe)
print(sentence_with_quotes)

# If you really need the same quote inside, escape it with a backslash
escaped = 'It\'s also possible, but harder to read'
print(escaped)

# Strings can be joined with +, and repeated with *
first_name = "Ada"
last_name = "Lovelace"
print(first_name + " " + last_name)
print("-" * 30)

# What to remember
# 1. ' and " are interchangeable
# 2. Pick the quote that lets you avoid backslashes
# 3. + joins strings, * repeats them
