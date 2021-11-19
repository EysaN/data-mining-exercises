"""
Task 4: open a csv file containing header and store its content in an array of dictionaries (name, age,
school). Calculate the average age of students for each school
"""

import csv
from itertools import groupby

with open('students.csv', newline='') as csv_file:
    csv_data = csv.DictReader(csv_file)
    data_list = [row for row in csv_data]
    list_of_ages = [int(row['age']) for row in data_list]
    print('total avg = ', sum(list_of_ages)/len(list_of_ages))
    data_groups = dict()
    for row in data_list:
        k, v = row['class'], int(row['age'])
        if k in data_groups:
            data_groups[k].append(v)
        else:
            data_groups[k] = [v]

    print('\n'.join(['avg by class {} = {}'.format(k, sum(v) / len(v)) for k, v in data_groups.items()]))
