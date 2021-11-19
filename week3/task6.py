"""
Create a nested dictionary using the dict() constructor for storing employee data. Write a
function having 2 input parameters and returning the given employee’s given data. Example
dictionary:
"""
_dict = {
            'emp1': {'name': 'Bob', 'job': 'Mgr'},
            'emp2': {'name': 'Kim', 'job': 'Dev'},
            'emp3': {'name': 'Sam', 'job': 'Dev'},
            'emp4': {'name': 'Sara', 'job': 'Assistan'},
            'emp5': {'name': 'Frid', 'job': 'Assistant'},
            'emp6': {'name': 'Patty', 'job': 'Senior Dev'},
            'emp7': {'name': 'Rony', 'job': 'Clrek'},
            'emp8': {'name': 'Dan', 'job': 'Mgr'},
            'emp9': {'name': 'David', 'job': 'Dev'},
            'emp10': {'name': 'Janos', 'job': 'Customer Care'},
            'emp11': {'name': 'Zoltan', 'job': 'Dev'}
        }


def dataquery(input1, input2):
    return _dict[input1.lower()][input2.lower()]


if __name__ == '__main__':
    print(dataquery('emp7', 'name'))
