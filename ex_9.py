#!/usr/bin/env python3

# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.
import random

def extra(number):
    print('Extra Exercise:\n')
    while True:
        guess = int(input('I have picked a number between 1 - 9. Can you guess it?\n'))
        if guess == number:
            while True:
                leave = str(input('Your answer was correct! Now type "exit" without quotes to leave.\n'))
                if leave == 'exit':
                    break
                else:
                    continue
            break
        elif guess < number:
            print('Too low')
            continue
        elif guess > number:
            print('Too high')


def main():
    print('Main Exercise:\n')
    number = random.randint(1,9)
    while True:
        guess = int(input('I have picked a number between 1 - 9. Can you guess it?\n'))
        if guess == number:
            print('You guessed it!')
            break
        elif guess < number:
            print('Too low')
            continue
        elif guess > number:
            print('Too high')
    extra(number)

if __name__ == '__main__':
    main()