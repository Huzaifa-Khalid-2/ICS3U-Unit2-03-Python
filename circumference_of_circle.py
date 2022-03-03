#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: March 2022
# This program calculates the circumference of a circle
#    with user input


import constants


def main():
    # this function calculates the circumference

    # input
    radius = int(input("Enter radius of the circle (mm): "))

    # process
    circumference = constants.TAU * radius

    # output
    print("circumference is {} mm².".format(circumference))
    print("\nDone")


if __name__ == "__main__":
    main()
