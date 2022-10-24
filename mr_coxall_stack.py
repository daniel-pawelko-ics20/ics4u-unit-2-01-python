#!/usr/bin/env python3

# Created on: Oct-2022
# Created by: Daniel Pawelko
# Created for: ICS4U
# This class creates an integer stack


class MrCoxallStack:
    # create the stack as a List
    stack_as_list = []

    def push(self, pushed_number: int):
        # add a number ot the list
        self.stack_as_list.append(pushed_number)

    def show_stack(self):
        # print out the stack to the console
        print(self.stack_as_list)
