"""
Write a Python program to find the type of the progression (arithmetic
progression/geometric progression) and the next successive member of a given three successive
members of a sequence.
An arithmetic progression (AP) is a sequence of numbers such that the difference of any two
successive members of the sequence is a constant. E.g.: 3, 5, 7, 9, 11, 13.
A geometric progression (GP) is a sequence of numbers where each term after the first is found by
multiplying the previous one by a fixed non-zero number called the common ratio. E.g.: 2, 6, 18, 54
"""


def get_progression_type(n_list):
    if n_list is None or not isinstance(n_list, list):
        n_list = []
    if len(set(n_list)) == 1:
        return 'not', n_list[1]
    n_list = [n for n in n_list if isinstance(n, int)]
    # find the list of differences between list elements
    reversed_n_list = n_list[::-1]
    diffs = [reversed_n_list[i] - n for i, n in enumerate(reversed_n_list[1:])]
    if len(set(diffs)) == 1:
        return 'arithmetic', n_list[-1]+int(diffs[0])
    ratios = [reversed_n_list[i] / n for i, n in enumerate(reversed_n_list[1:])]
    if len(set(ratios)) == 1:
        return 'geometric', n_list[-1]*int(ratios[0])
    return 'unknown', None


if __name__ == '__main__':
    tests = [[3, 5, 7, 9, 11, 13],
             [2, 6, 18, 54],
             [1, 2, 3],
             [2, 6, 18],
             [0, 0, 0]
    ]
    for test in tests:
        _type, _next = get_progression_type(test)
        print('numbers %s are of %s progression, and next sequence is %s' % (test, _type, _next))


