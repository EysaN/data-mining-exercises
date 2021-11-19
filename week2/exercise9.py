"""
Count determiners (a and an) in a string
"""
import re


def count_det(x):
    if x is None:
        print("A text must be provided")
    list_of_words = x.split(' ')
    print('count of a=', len([w for w in list_of_words if re.sub('\W+', ' ', w.lower()).strip() == 'a']))
    print('count of an=', len([w for w in list_of_words if re.sub('\W+', ' ', w.lower()).strip() == 'an']))
    print('count of the=', len([w for w in list_of_words if re.sub('\W+', ' ', w.lower()).strip() == 'the']))


if __name__ == "__main__":
    print("enter your sentance:")
    sentance = input()
    count_det(sentance)
