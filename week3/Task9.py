"""
Write a Python program to find the digits which are absent in a given mobile number.
"""


def find_absent_numbers(mobile):
    if mobile is None or not isinstance(mobile, str):
        mobile = ''
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('You entered: ', mobile)
    mobile_list = [int(n) for n in mobile if n.isnumeric()]
    return [n for n in numbers if n not in mobile_list]


if __name__ == '__main__':
    print('enter a mobile number:')
    mobile_num = input()
    print('Unfound numbers = ', find_absent_numbers(mobile_num))
