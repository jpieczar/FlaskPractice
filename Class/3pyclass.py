class Employee:

    raise_amount = 1.04
    num_of_employes = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (first.lower() + '.' + last.lower() + "@company.com")
        Employee.num_of_employes += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    
    # Turning a regular method into a classmethod.
    @classmethod # This here is a decorator.
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    # Below we will use a static method because it does not rely on
    # any other piece of data. It does not take in an instance nor
    # a class (self and cls respectively).
    @staticmethod
    def is_workday(day): # Inside the bracket is only the used parameter.
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

import datetime
my_date = datetime.date(2020, 1, 18)
print(Employee.is_workday(my_date))

# emp_1_str = "Jonathan-Pieczara-60000"
# emp_2_str = "Test-McTest-60000"
# emp_3_str = "Bob-Martin-42000"
# emp_4_str = "Lisa-Example-35000"

# emp_1 = Employee.from_string(emp_1_str)
# emp_2 = Employee.from_string(emp_2_str)
# emp_3 = Employee.from_string(emp_3_str)
# emp_4 = Employee.from_string(emp_4_str)

# print(emp_1.fullname())
# print(emp_2.fullname())
# print(emp_3.fullname())
# print(emp_4.fullname())

# emp_2 = Employee("Test", "McTest", 60000)
# emp_1 = Employee("Jonathan", "Pieczara", 60000)

# print(emp_1.pay)
# print(emp_2.pay)
# print("---")
# emp_1.apply_raise()
# print(emp_1.pay)
# print(emp_2.pay)
# print("---")
# Employee.set_raise_amount(2)
# emp_1.apply_raise()
# emp_2.apply_raise()
# print(emp_1.pay)
# print(emp_2.pay)