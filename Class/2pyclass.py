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
    
    def appy_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("Jonathan", "Pieczara", 60000)
emp_2 = Employee("Test", "McTest", 60000)
emp_3 = Employee("Tset", "TsetCm", 60000)

print(emp_1.pay)
emp_1.appy_raise()
print(emp_1.pay)

Employee.raise_amount = 1.05 # Changes for all employees.
emp_2.raise_amount = 1.05 # Changes only for emp_2.

print(emp_2.pay)
emp_2.appy_raise()
print(emp_2.pay)

print(Employee.num_of_employes)