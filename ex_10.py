#!/usr/bin/env python3

# This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.

# Take two lists, say for example these two:

# 	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# 	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
# Make sure your program works on two lists of different sizes. Write this using at least one list comprehension. (Hint: Remember 
# list comprehensions from Exercise 7).
import random

def main():
    a = []
    b = []
    duplicates = []
    for i in range(0,9):
        random_a = random.randint(1,30)
        random_b = random.randint(1,30)
        a.append(random_a)
        b.append(random_b)
    print(a)
    print(b)
    set_a = set(a)
    set_b = set(b)
    unique = True
    for item in set_a:
        if item in set_b:
            duplicates.append(item)
            unique = False
    if unique == True:
        print('Both lists have all unique numbers')
    else:
        print(f'These values are in both: {duplicates}')

if __name__ == '__main__':
    main()