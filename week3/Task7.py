"""
How to implement a switch-case in Python
"""


def switcher(argument):
    # Dictionary definition
    switchdate = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return switchdate.get(argument, "Invalid month")


if __name__ == '__main__':
    print(switcher(2))
