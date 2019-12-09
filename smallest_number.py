#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: Dec 2019
# This program finds the lowest number from random numbers.

import random


def smallest_number(list_of_numbers):
    # this functions finds the largest number

    small_num = list_of_numbers[0]

    for counter in list_of_numbers:
        if counter < small_num:
            small_num = counter

    return small_num


def main():
    # this function generates random numbers

    random_numbers = []
    small_num = 0

    # input
    print("The numbers are ")
    for loop_counter in range(0, 9):
        a_single_number = random.randint(0, 10)
        random_numbers.append(a_single_number)
        print("{0}, ".format(a_single_number), end="")
    print("")

    small_num = smallest_number(random_numbers)

    print("The biggest number is: {0} ".format(small_num))


if __name__ == "__main__":
    main()
