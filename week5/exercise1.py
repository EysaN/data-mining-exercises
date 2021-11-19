"""
Create a NumPy 2D array and insert values at random positions.
a. Calculate row-wise sum of values.
b. Create a new array with row-wise counts of possible values.
"""
import numpy as np
from numpy import random


two_d_arr = random.choice(range(10), size=(5, 5))
print('original array:\n', two_d_arr)

row_sum_arr = np.zeros([5, 1], dtype=int)
row_counts_arr = np.zeros_like(two_d_arr)

for i, row in enumerate(two_d_arr):
    np.put(row_sum_arr, i, row.sum(axis=0))
print('row wise sum:\n', row_sum_arr)

new_arr, inds, counts = np.unique(two_d_arr, return_index=True, return_counts=True)
np.put(row_counts_arr, inds, counts)
print('row wise counts of values:\n', row_counts_arr)
