#!/usr/bin/env python3
# Ask the user for a number and determine whether the number is prime or not. 
# (For those who have forgotten, a prime number is a number that has no divisors.). 
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity 
# to practice using functions, described below.

def main():
    number = int(input('Pick a number:\n'))
    divisors = []
    prime = True
    for i in range(2, number):
        if number % i == 0:
            prime = False
            divisors.append(i)
    if prime == True:
        print(f'{number} is a prime number.')
    else:
        print(f'This number is not prime, because the following are divisors: {divisors}')

if __name__ == '__main__':
    main()