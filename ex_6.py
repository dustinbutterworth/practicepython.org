#!/usr/bin/env python3
# Ask the user for a string and print out whether this string is a 
# palindrome or not. (A palindrome is a string that reads the same 
# forwards and backwards.)

def main():
    word = str(input('Please provide a word:\n'))
    reversed_word = word[::-1]
    if word == reversed_word:
        print(f'{word} is a palindrome!')
    else:
        print(f'{word} is not a palindrome.')

if __name__ == '__main__':
    main()