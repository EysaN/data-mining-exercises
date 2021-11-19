"""
Guess my number
"""
from random import seed
from random import randint

# seed random number generator
seed(1)
my_number = randint(0, 10)
user_guess = 0
while user_guess != my_number:
    print('Can you guess my number?')
    user_guess = int(input())
    if user_guess > my_number:
        print('smaller')
    elif user_guess < my_number:
        print('greater')
print('You have correctly guessed my number!')