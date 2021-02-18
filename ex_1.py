#!/usr/bin/env python3
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:

# Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
import datetime
from dateutil.relativedelta import relativedelta

def age_calc(name,age):
    year = datetime.date.today()
    total_years = 100 - age
    hundred_years = year + relativedelta(years=total_years)
    return hundred_years.strftime('%Y')


def main():
    name = input('What is your name?\n')
    age = int(input('\nWhat is your age?\n'))
    print(f'\n{name}, you said you are {age} years old.\n')
    answer_year = age_calc(name,age)
    print(f'You will turn 100 in {answer_year}\n')
    repeater = int(input('How many times would you like to see this message again?\n'))
    print(repeater * f'You will turn 100 in {answer_year}\n')

if __name__ == '__main__':
    main()