"""
Create a file with one word in each row (or list of words). Read out the words and place them in a
list in groups according to their first character. That is, words starting with ‘a’ go under the first
position, words starting with ‘b’ go under the second position, etc.
"""

from itertools import groupby

with open('task1-words', 'r') as data:
    words = data.read().splitlines()
_dict = dict()
for k, g in groupby(words, key=lambda x: x[0]):
    if k in _dict:
        _dict[k].extend(list(g))
    else:
        _dict[k] = list(g)
print([list(_dict[k]) for k in sorted(_dict)])
