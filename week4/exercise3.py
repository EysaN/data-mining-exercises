"""
Let’s build simple central authentication and authorization system. Add Users and check the validity
of passwords
"""

from random import randint
import csv


_chars = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
          'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_', '#', '&', '@', '$', '!']


def generate_pass():
    return ''.join([str(_chars[randint(0, len(_chars)-1)]) for _ in range(16)])


class AccessError(Exception):
    def __init__(self, msg):
        print(msg)


class User:
    def __init__(self, name, username, password=None, role='user'):
        self.name = name
        self.username = username
        self.password = generate_pass() if password is None or password == '' else password
        self.role = 'user' if role is None or role == '' else role


user_dict = dict()
fieldnames = []
with open('userdb.csv', newline='') as csv_data:
    csv_dict = csv.DictReader(csv_data)
    fieldnames = csv_dict.fieldnames
    for row in csv_dict:
        user_dict[row['username']] = User(row['username'], row['name'], row['pass'], row['role'])


def add_user(user):
    if user.role == 'admin':
        raise AccessError('You are not allowed to create admins')
    with open('userdb.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({fieldnames[0]: user.username, fieldnames[1]: user.name, fieldnames[2]: user.password, fieldnames[3]: user.role})
        for ud in list(user_dict.values()):
            writer.writerow({fieldnames[0]: ud.username, fieldnames[1]: ud.name, fieldnames[2]: ud.password, fieldnames[3]: ud.role})
    print('new user %s is added' % user.name)


def validate(username, password):
    if user_dict.get(username) is None:
        raise AccessError('User Not Found')

    if password == user_dict[username].password:
        print('Cool! %s is authenticated' % user_dict[username].name)
    else:
        raise AccessError('User is not validated')


if __name__ == '__main__':
    try:
        print('available actions on users are: create, validate, close')
        action = ''
        while action != 'close':
            print('choose an action')
            action = input()
            if action == 'create':
                print('enter a name')
                name = input()
                print('enter a username')
                username = input()
                print('enter a password or leave it empty to auto create it')
                password = input()
                print('choose a role')
                role = input()
                new_user = User(name, username, password, role)
                add_user(new_user)
            elif action == 'validate':
                print('enter your username')
                username = input()
                print('enter your password')
                password = input()
                validate(username, password)
            elif action == 'close':
                print('Goodbye')
            else:
                print('action is recognized')
    except AccessError as e:
        print(e)
