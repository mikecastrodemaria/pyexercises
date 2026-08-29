"""Histogram (bonus).

A histogram counts how many values fall into each range. It is the fastest
way to see the shape of a dataset.

Needs: pip install numpy matplotlib
"""

import numpy
import matplotlib
matplotlib.use("Agg")          # draw to a file, there is no window in a Codespace
import matplotlib.pyplot as plt
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(HERE, "histogram.png")

values = numpy.random.uniform(0.0, 5.0, 250)

plt.figure(figsize=(8, 4))
plt.hist(values, bins=5, edgecolor="white")
plt.title("250 values between 0 and 5, in five buckets")
plt.xlabel("value")
plt.ylabel("how many")
plt.tight_layout()
plt.savefig(OUTPUT, dpi=120)

print("image written:", OUTPUT)
print("open it from the file explorer on the left")

# Try changing bins to 20 and running it again. Same data, different story.

# What to remember
# 1. bins decides how many buckets, and it changes what you see
# 2. In a Codespace there is no window, so you save the chart to a file
# 3. A chart is a way to check your data, not only a way to present it
