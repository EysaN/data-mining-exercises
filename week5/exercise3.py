"""
3. Count unique values in an array.
"""
import numpy as np


test_arr = np.array([[4, 3, 3, 0, 1],
                     [4, 3, 3, 0, 1],
                     [10, 12, 5, 2, 2],
                     [10, 14, 13, 77, 8],
                     [4, 5, 6, 36, 8]])

res, counts = np.unique(test_arr, return_counts=True)
print('unique values are:\n', [x for x, y in zip(res, counts) if y == 1])
