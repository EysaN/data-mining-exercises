"""
Write a basic calculator program. The input is a mathematical expression to solve, for example
„4 * 7”. Calculate the result for the basic arithmetic functions (addition, substraction,
multiplication, division). Avoid dividing with 0
"""


def calculate(_exp):
    if _exp is None:
        return
    result = "NA"
    try:
        result = eval(_exp)
    except ZeroDivisionError:
        print("cannot divide by zero")
    except (SyntaxError, NameError):
        print("invalid expression, only digits and operators are allowed")
    return result


if __name__ == '__main__':
    exp = ""
    while 1:
        print("enter a mathematical expression to solve or 0 to quit:")
        exp = input()
        if exp == "0":
            break
        print(calculate(exp))
