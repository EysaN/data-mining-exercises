"""
Write a Python program which adds up columns and rows of a given table
"""
import sys


def sum_table(table):
    if table is None or not isinstance(table, str):
        table = ''

    arr = [[int(v) for v in row.split(',')] for row in table.split(';')]
    print('Your input is\n%s' % arr)
    result = ''
    sum_columns = ['0' for _ in arr[0]]
    for i, item in enumerate(arr):
        row_sum = sum(item)
        result += '\t'.join([str(v) for v in item]) + '\t' + str(row_sum) + '\n'
        sum_columns = [int(col) + it for it, col in zip(item, sum_columns)]
        if len(arr) - i == 1:
            result += '\t'.join([str(v) for v in sum_columns]) + '\t' + str(row_sum + sum(sum_columns))
    return result


if __name__ == '__main__':
    print('enter a number or rows/columns:')
    count_rows_cols = int(input())
    if not isinstance(count_rows_cols, int):
        print('you should enter a number, try again')
        sys.exit(0)
    print('enter {0} rows seperated by semi-colons\nwhere each row has {0} volues seperated by commas'.format(count_rows_cols))
    array_input = input()
    print('result is: \n', sum_table(array_input))
