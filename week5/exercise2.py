"""
2. Find the position of missing values in the array.
a. Replace missing values with 0.
b. Drop the missing values / drop the rows with missing values.
c. Find duplicate values / rows in the array
"""
import numpy as np

nan = np.nan
test_arr = np.array([[4, 3, 3, 0, 1],
                     [4, 3, 3, 0, 1],
                     [10, 12, 5, 2, 2],
                     [10, 14, nan, 77, 8],
                     [4, 5, 6, nan, 8]])
# 2
missing_values = np.where(np.isnan(test_arr))
print('missing values indices:', missing_values[-1])

# a
test_a = test_arr.copy()
for i, j in zip(missing_values[0], missing_values[-1]):
    np.put(test_a[i], j, 0)
print('missing values replaced:\n', test_a)

# b
# Drop the missing values
filtered = test_arr[~np.isnan(test_arr)]
print('dropped missing values\n', filtered)
# drop the rows with missing values
test_b = np.empty((0, 5), int)
for i, row in enumerate(test_arr):
    if len(row[np.isnan(row)]) == 0:
        test_b = np.append(test_b, np.array([row]), axis=0)
print('dropped rows with missing values:\n', test_b)

# c
# Find duplicate values
test_c = test_arr.copy()
res, counts = np.unique(test_c, return_counts=True)
print('dubplicate values are:\n', [x for x, y in zip(res, counts) if y > 1])
# Find dubplicate rows
res, counts = np.unique(test_c, return_counts=True, axis=0)
print('dubplicate rows are:\n', [x for x, y in zip(res, counts) if y > 1])








