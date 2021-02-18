#!/usr/bin/env python3
# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
import random

# Not as oneliner
def extra1():
    a = []
    b = []
    for i in range(0,9):
        random_a = random.randint(1,99)
        random_b = random.randint(1,99)
        a.append(random_a)
        b.append(random_b)
    print(a)
    print(b)
    set_a = set(a)
    set_b = set(b)
    unique = True
    for item in set_a:
        if item in set_b:
            print(f'{item} is in both lists')
            unique = False
    if unique == True:
        print('Both lists have all unique numbers')


def extra2():
    print([x for x in range(1, random.randint(1,30)) if x in range(1, random.randint(1,30)) ])


def main():
    print('Main Exercise:')
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    set_a = set(a)
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    set_b = set(b)
    for item in set_a:
        if item in set_b:
            print(f'{item} is in both lists')
    print('\nExtra 1:')
    extra1()
    print('\nExtra 2:')
    extra2()

if __name__ == '__main__':
    main()