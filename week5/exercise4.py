"""
4. Calculate mean, median, moving average and modus (most frequent value) of a 1D array.
"""
import numpy as np

test_arr = np.array([4, 3, 3, 0, 1, 10, 12, 5, 2, 4, 10, 14, 13, 77, 8, 4, 5, 6, 36, 8])

print('mean = ', np.mean(test_arr))
print('median = ', np.median(test_arr))
print('moving average = ', np.array([cs/(i+1) for i, cs in enumerate(np.cumsum(test_arr))]))
new_arr, inds, counts = np.unique(test_arr, return_index=True, return_counts=True)
print('modus = ', list(new_arr)[list(counts).index(max(counts))])
