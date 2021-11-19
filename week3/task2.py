"""
Consider the case of recording temperature for 1 week measured in the morning, mid-day, evening
and mid-night. It can be presented as a 7X5 matrix using an array. Write a function that finds the
maximum / minimum values in the matrix.
"""

import numpy as np


temperature = [
    [10, 31, 15, 11],
    [9, 33, 26, 12],
    [8, 25, 24, 10],
    [11, 31, 20, 11],
    [16, 28, 22, 8],
    [15, 24, 19, 2],
    [14, 32, 19, 13]
]


def find_max_min(arr):
    print('maximum value = ', np.amax(arr))
    print('minimum value = ', np.amin(arr))


if __name__ == '__main__':
    find_max_min(temperature)
