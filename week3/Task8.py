"""
Write a Python program to find unique triplets whose three elements gives the sum of zero
from an array of n integers.
"""


def find_zero_sum_triples(n_list):
    if n_list is None or not isinstance(n_list, list):
        n_list = []
    n_list = [n for n in n_list if isinstance(n, (int, float))]
    print('original list = ', n_list)
    triples = [n_list[n-3:n] for n in range(3, len(n_list)+1)]
    print('possible triples = ', triples)
    results = []
    for triple in triples:
        if sum(triple) == 0:
            results.append(triple)
    return results


if __name__ == '__main__':
    print('result = ', find_zero_sum_triples([1, 3, 'as', [343], {'name': 1}, 1.9, -4, 15, 2, 0, 2, -12, 7, 5, 0, 0, 0]))
