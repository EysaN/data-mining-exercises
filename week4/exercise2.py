"""
Let’s build a class hierarchy. Person → Adult → Employee. Person → Child. Adults and children
are differentiated based on their age. An Employee is an adult having a job.
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Person init')


class Adult(Person):
    def __init__(self, name, age, job):
        super().__init__(name, age)
        self.job = job
        print('Adult init')


class Employee(Adult):
    def __init__(self, name, age, job, salary):
        super().__init__(name, age, job)
        self.salary = salary
        print('Employee init')


class Child(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
        print('Child init')


if __name__ == '__main__':
    print('enter your name')
    name = input()
    print('enter your age')
    age = int(input())
    if age <= 0:
        raise ValueError('age should be positive')
    else:
        if age <= 18:
            print('Child record has been detected')
            print('enter your school')
            school = input()
            Child(name, age, school)
        else:
            print('enter your job')
            job = input()
            if job is None or job == '':
                Adult(name, age, '')
            else:
                print('enter your salary')
                salary = input()
                Employee(name, age, job, salary)

