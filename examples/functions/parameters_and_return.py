"""Parameters and return values."""

def compute_ctr(clicks, impressions):
    """Returns the click-through rate as a ratio between 0 and 1."""
    return clicks / impressions

print("CTR:", compute_ctr(4838, 283000))

print("-" * 30)

# Default values: the caller may leave them out
def format_percentage(ratio, decimals=2):
    """Turns a ratio into a readable percentage."""
    return f"{ratio * 100:.{decimals}f} %"

print(format_percentage(0.0171))
print(format_percentage(0.0171, 4))

print("-" * 30)

# Naming the arguments makes a long call readable
def describe(name, channel, conversions):
    return f"{name} on {channel}: {conversions} conversions"

print(describe(name="Winter Sale", channel="Meta Ads", conversions=290))

print("-" * 30)

# Returning several values at once
def minimum_and_maximum(values):
    """Returns the smallest and the largest value."""
    return min(values), max(values)

low, high = minimum_and_maximum([5, 2, 8, 1])
print("low:", low, "| high:", high)

print("-" * 30)

# Guard clause: deal with the impossible case first, then the normal one
def compute_cpa(cost, conversions):
    """Returns the cost per conversion, or None when there is no conversion."""
    if conversions == 0:
        return None
    return cost / conversions

print("normal case:", compute_cpa(11088.60, 290))
print("zero case  :", compute_cpa(11088.60, 0))

# What to remember
# 1. A parameter with a default value can be left out by the caller
# 2. A function can return several values, separated by commas
# 3. Handling the impossible case first keeps the rest of the function simple
