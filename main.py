#!/usr/bin/env python3

# Created on: Oct-2022
# Created by: Daniel Pawelko
# Created for: ICS4U
# This program uses the MrCoxallStack

from mr_coxall_stack import MrCoxallStack


def main():
    # this function uses the MrCoxallStack
    my_new_stack = MrCoxallStack()

    try:
        some_number = int(input("Enter and integer: "))
        my_new_stack.push(some_number)
        my_new_stack.show_stack()
    except:
        print("Input Invalid :(")

    print("\nDone.")


if __name__ == "__main__":
    main()
