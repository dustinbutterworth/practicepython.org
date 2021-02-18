#!/usr/bin/env python3
# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropriate message to the user. Hint: how does an even / odd 
# number react differently when divided by 2?

# Extras:

# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) 
# and one number to divide by (check). If check divides evenly into num, 
# tell that to the user. If not, print a different appropriate message.

def extra():
    num = int(input("Give me a number:\n"))
    check = int(input("Pick a number to divide by:\n"))
    if num % check == 0:
        print(f'\n{check} divides evenly into {num}')
    else:
        print(f'\n{check} does not divide evenly into {num}')


def main():
    number = int(input('Please choose a number:\n'))
    if number % 4 == 0:
        print(f'{number} is a multiple of 4')
    elif number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')
    extra()

if __name__ == '__main__':
    main()