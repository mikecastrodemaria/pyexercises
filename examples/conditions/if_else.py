"""Making the program choose.

An if block runs only when its test is true. This is how a program reacts.
"""

age = 20

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

print("-" * 30)

# Several cases: if, then elif as many times as needed, then else
score = 4

if score == 5:
    print("Perfect.")
elif score >= 3:
    print("Good result.")
elif score >= 1:
    print("You got some right.")
else:
    print("Nothing right this time.")

print("-" * 30)

# Combining tests with and / or / not
impressions = 283000
conversions = 0

if impressions > 0 and conversions > 0:
    print("This campaign can be measured on cost per conversion.")
if impressions == 0 or conversions == 0:
    print("Careful: one of the numbers is zero. A division would crash here.")

# Indentation is what defines the block. Python has no braces
if True:
    print("inside the block")
print("outside the block")

# What to remember
# 1. The colon and the indentation define the block
# 2. == compares, = assigns. Mixing them up is the most common beginner error
# 3. Test for zero BEFORE dividing
