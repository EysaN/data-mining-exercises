"""
Slicing a string. Check if a sentence is correct. A sentence is correct if starts with big capital
letter and ends with a punctuation mark.
"""


def is_sentance_correct(x):
    if x[0] == str(x[0]).upper() and x[-1] == '!':
        return "sentance is correct"
    return "sentance is not correct"


if __name__ == "__main__":
    print("A sentence is correct if starts with big capital letter and ends with a punctuation mark")
    print("enter your sentance:")
    sentance = input()
    print(is_sentance_correct(sentance))