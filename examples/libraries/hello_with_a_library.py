"""Hello World, twice: once with Python alone, once with a library.

Same output, same idea, two different amounts of work. This is the whole point of
a library: somebody already wrote the boring part, and you reuse it.

Before running this file, install the library. In the terminal at the bottom of your
Codespace, type:

    pip install cowsay

Then run this file. If you get ModuleNotFoundError, you skipped that line.
"""

# ---------------------------------------------------------------------------
# 1. Python alone. print() is built in, nothing to install
# ---------------------------------------------------------------------------

print("Hello, World!")

print("-" * 30)

# ---------------------------------------------------------------------------
# 2. Drawing a frame around it, by hand. Still Python alone, but now it is work
# ---------------------------------------------------------------------------

message = "Hello, World!"

# We compute the width once, so the frame fits whatever the message is
width = len(message) + 2

print("+" + "-" * width + "+")
print("| " + message + " |")
print("+" + "-" * width + "+")

print("-" * 30)

# ---------------------------------------------------------------------------
# 3. The same job, with a library somebody else wrote
# ---------------------------------------------------------------------------

# import makes the library available under the name that follows
import cowsay

cowsay.cow("Hello, World!")

print("-" * 30)

# The library also knows other characters. You did not write any of this
cowsay.dragon("A library is code you did not write, and did not have to")

print("-" * 30)

# ---------------------------------------------------------------------------
# 4. Where does it actually live?
# ---------------------------------------------------------------------------

# A library is a file on the machine that runs your code, nothing magic.
# This prints the exact path, inside your Codespace
print("cowsay is installed here:")
print(cowsay.__file__)

# What to remember
# 1. pip install downloads a library into the machine running your code.
#    In a Codespace, that is the Codespace, not your own computer and not your repository
# 2. import makes it usable in this file. Installing is not importing, you need both
# 3. Somebody else maintains that code. That is the deal: less work for you,
#    one more thing that can change or break without warning you
# 4. If you hand this file to a colleague who has not installed cowsay, it crashes.
#    That is why real projects list what they need in a file called requirements.txt
