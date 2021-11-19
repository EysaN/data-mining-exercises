"""
List statistics: write a function for counting each element of a list and print out the statistics
to stdout / file / return this list of counts:
    - Greatest pair in list: create all pairs of a list and select the pair with greatest sum.
    - Closest to average: find the element of a list which is closest to the list average.
    - Check if the elements in a list are monotone increasing / decreasing
"""
import sys


def list_stats(data):
    # counting each element of a list
    if data is None:
        sys.exit(0)
    elem_counts = dict()
    numbers = [int(d) for d in data]
    list_avg = sum(numbers)/len(numbers)
    closest_to_avg, a, b, monotone = 0, 0, 0, []
    for i, num in enumerate(numbers):
        # counting each element of a list
        if elem_counts.get(num):
            elem_counts[num].append(i)
        else:
            elem_counts[num] = [i]

        if i == 0:
            a = abs(num - list_avg)
            b = num
        else:
            # Closest to average: find the element of a list which is closest to the list average.
            if abs(num - list_avg) <= a:
                closest_to_avg = num
                a = abs(num - list_avg)

            # Check if the elements in a list are monotone increasing / decreasing.
            if b < num:
                monotone.append(1)
            elif b > num:
                monotone.append(-1)
            else:
                monotone.append(0)
            b = num

    # Greatest pair in list: create all pairs of a list and select the pair with greatest sum
    temp = numbers
    temp.sort()
    great_paid_sum = temp[-2:]
    temp.clear()

    print('input is:', data)
    print('output:')
    print('count of each element: ', [[k, len(v)] for k, v in elem_counts.items()])
    print('greatest pair=', great_paid_sum)
    print('avg=', list_avg)
    print('closest to avg=', closest_to_avg)

    if sum(monotone) == 0 or abs(sum(monotone)) != len(monotone):
        print("list is not monotone increasing nor decreasing.")
    elif sum(monotone) > 0:
        print("list is monotone increasing.")
    elif sum(monotone) < 0:
        print("list is monotone decreasing.")
    else:
        print("list is not recognized")


if __name__ == "__main__":
    print("enter some numbers seperated by commas, non numeric values will be ignored")
    _list = input()
    list_stats([li for li in _list.strip().split(',') if li.isnumeric()])
