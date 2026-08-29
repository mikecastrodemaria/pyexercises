"""Floats.

Numbers with a decimal point. Python calls this type float.
"""

cost = 11088.60
conversions = 290

cpa = cost / conversions
print("cost         :", cost)
print("type         :", type(cost))
print("cost per conversion:", cpa)

# Rounding for display
print("round(cpa, 2):", round(cpa, 2))
print("formatted    :", f"{cpa:.2f} EUR")

# Careful: floats are approximations
print("0.1 + 0.2    :", 0.1 + 0.2)
print("is it 0.3?   :", 0.1 + 0.2 == 0.3)
print("safer test   :", abs((0.1 + 0.2) - 0.3) < 0.000001)

# European files write amounts with a comma. Python needs a dot
amount_from_file = "11088,60"
amount = float(amount_from_file.replace(",", "."))
print("converted    :", amount)

# What to remember
# 1. round() is for display, it does not make a float exact
# 2. Never compare two floats with ==, compare the difference
# 3. A European amount needs its comma replaced before float()
