"""Condition-controlled loops.

A while loop repeats as long as its test stays true.
Use it when you do not know in advance how many times you will loop.
"""

count = 0
while count < 5:
    print("iteration", count + 1)
    count = count + 1     # forget this line and the loop never ends

print("-" * 30)

# The classic use: keep asking until the answer is acceptable.
# Uncomment to try it interactively.
# answer = ""
# while answer not in ("yes", "no"):
#     answer = input("Continue? (yes/no) ").strip().lower()
# print("You answered", answer)

# while True with a break is often the most readable form
attempts = 0
while True:
    attempts = attempts + 1
    print("attempt", attempts)
    if attempts >= 3:
        break

print("-" * 30)

# A safety counter avoids an infinite loop while you are testing
safety = 0
value = 100
while value > 1:
    value = value / 2
    safety = safety + 1
    if safety > 50:
        print("something is wrong, stopping")
        break
print("halved", safety, "times, final value:", round(value, 4))

# What to remember
# 1. Something inside the loop must eventually make the test false
# 2. while True + break is fine, and often clearer
# 3. If your program hangs, you wrote an infinite loop. Stop it with the bin icon in the terminal
