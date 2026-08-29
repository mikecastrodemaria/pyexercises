"""Data distribution (bonus).

Real datasets are large. To practise, you generate numbers yourself and
look at how they spread out.

Needs: pip install numpy
"""

import numpy

# 250 random values between 0 and 5
values = numpy.random.uniform(0.0, 5.0, 250)

print("how many values :", len(values))
print("first ten       :", numpy.round(values[:10], 2))
print("smallest        :", round(values.min(), 2))
print("largest         :", round(values.max(), 2))
print("average         :", round(values.mean(), 2))
print("median          :", round(numpy.median(values), 2))
print("standard deviation:", round(values.std(), 2))

# A normal distribution: values gathered around an average
ages = numpy.random.normal(40, 10, 250)
print()
print("ages, average   :", round(ages.mean(), 1))
print("ages, deviation :", round(ages.std(), 1))

# What to remember
# 1. The average alone says little. The spread matters as much
# 2. The median resists extreme values better than the average
# 3. A NumPy array is not a Python list, but it behaves in a similar way
