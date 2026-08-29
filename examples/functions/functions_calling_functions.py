"""Functions calling other functions.

This is how a real program is built: small functions, and one that coordinates them.
"""

def is_even(number):
    """True when the number divides by two exactly."""
    return number % 2 == 0

def is_zero(number):
    """True when the number is zero."""
    return number == 0

def describe(number):
    """Uses the two functions above to describe one number."""
    if is_zero(number):
        return f"{number} is zero"
    if is_even(number):
        return f"{number} is even"
    return f"{number} is odd"

for value in [0, 3, 8, -4]:
    print(describe(value))

print("-" * 30)

# The main() pattern: one function that runs the program
def load_scores():
    """Pretends to load scores. In the final project this reads a file."""
    return {"Alice": 4, "Bob": 2}

def best_player(scores):
    """Returns the name holding the highest score."""
    return max(scores, key=scores.get)

def main():
    """Runs the whole program, step by step."""
    scores = load_scores()
    print("scores :", scores)
    print("winner :", best_player(scores))

# This line means: run main() only when this file is the one being executed
if __name__ == "__main__":
    main()

# What to remember
# 1. One function, one job. Its name should say that job
# 2. main() is where the order of operations lives
# 3. The if __name__ line is the standard way to start a Python program
