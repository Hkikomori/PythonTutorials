# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

import numpy as np


class Employee:
    # Class Variables, can be accased from the class or an instance
    raise_amount = 1.04
    num_of_employees = 1

    # Constructor
    def __init__(self, first, last, pay):
        self. first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@company-name.com'.format(self.first, self.last)
        self.fullname = '{} {}'.format(self.first, self.last)
        Employee.num_of_employees += 1

    # Methods
    def __repr__(self):
        return '{}, {} (Pay is {})'.format(self.fullname, self.email, self.pay)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


def Main():
    pass


if __name__ == '__main__':
    Main()
