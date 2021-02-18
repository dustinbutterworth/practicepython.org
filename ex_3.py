#!/usr/bin/env python3
# Take a list, say for example this one:
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:

# Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Not as a one liner
def extra1():
    global a
    less_than_five_list = []
    for item in a:
        if item < 5:
            less_than_five_list.append(item)
    print(f'Extra 1 - These numbers are less than 5: {less_than_five_list}')


# as a one liner
def extra2():
    print('Extra 2 - These numbers are less than 5:',[i for i in [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] if i < 5])


def extra3():
    global a
    less_than_five_list = []
    number = int(input('\nPick a number: \n'))
    for item in a:
        if item < number:
            less_than_five_list.append(item)
    print(f'Extra 3 - These numbers are less than {number}: {less_than_five_list}')


def main():
    global a
    for item in a:
        if item < 5:
            print(f'{item} is less than 5')
    extra1()
    extra2()
    extra3()

if __name__ == '__main__':
    main()