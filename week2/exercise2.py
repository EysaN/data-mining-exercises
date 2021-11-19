"""
Print Fibonacci series up to n
"""


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


if __name__ == '__main__':
    fib_n = ""
    inp = ""
    while inp != "0":
        print("Enter 1 for fib1 or 2 for fib2:")
        fib_n = input()
        print("Enter a number or 0 to quit:")
        inp = input()
        if inp.isnumeric():
            fib(int(inp)) if fib_n == "1" else print(fib2(int(inp)))
        else:
            print("not a number")
