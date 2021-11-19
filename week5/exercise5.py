"""
5. Filter the array based on two or more conditions.
"""
import numpy as np


test_arr = np.array([4, 3, 3, 1, 10, 12, 5, 2, 4, 10, 14, 13, 77, 8, 4, 5, 6, 36, 8])
# add as many coditions as needed in the filter array
filter_arr = np.array([test_arr % 2 == 0, test_arr > 0])
newarr = test_arr[np.all(filter_arr)]
print(newarr)
newarr = test_arr[np.any(filter_arr)]
print(newarr)
