"""
Write a Python program to get the Least Common Multiple (LCM) of more than two
numbers (any numbers). Take the numbers from a given list of positive integers.
"""
import numpy as np


def check_comman_value(_list, num):
    if len(_list) < num:
        return None
    results = set()
    for i, m in enumerate(_list):
        if i == 0:
            results = m
        else:
            results = set(m).intersection(results)
    return sorted(results)[0] if len(results) == 1 else None


def find_lcm(n_list):
    if n_list is None or not isinstance(n_list, list):
        n_list = []
    n_list = [int(n) for n in n_list if str(n).isnumeric()]
    all_multiplies = dict()
    while True:
        for item in n_list:
            if item in all_multiplies:
                new_item = item + all_multiplies.get(item)[-1]
                all_multiplies[item].append(new_item)
            else:
                all_multiplies[item] = [item]
        results = check_comman_value(list(all_multiplies.values()), len(n_list))
        if results:
            return results


if __name__ == '__main__':
    print('enter a list of numbers seperated by spaces:')
    data = input()
    print('lcm of (%s) = ' % data, find_lcm(data.split(' ')))

