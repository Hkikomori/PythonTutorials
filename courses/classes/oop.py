# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc


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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # Alternative Constructor
    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(date):
        return date.weekday() != 5 and date.weekday() != 6



class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


def Main():
    dev = Developer('peter', 'griffin', 1000, 'Python')


if __name__ == '__main__':
    Main()
