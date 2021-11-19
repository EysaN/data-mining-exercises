"""
Write a Python program to remove the duplicate elements of a given array of numbers
such that each element appears only once and return the new length of the given array
"""


def remove_dups(arr):
    if arr is None or not isinstance(arr, list):
        arr = []
    arr = [int(a) for a in arr if str(a).isnumeric()]
    return len(set(arr))


if __name__ == '__main__':
    print('enter a list of numbers seperated by spaces:')
    data = input()
    print('old length is = ', len(data.split(' ')))
    print('new len is = ', remove_dups(data.split(' ')))
