class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = (first.lower() + '.' + last.lower() + "@company.com")

    def fullname(self): # 'self' is used to work with all instances.
        return "{} {}".format(self.first, self.last)

emp_1 = Employee("Jonathan", "Pieczara", 60000)
emp_2 = Employee("Test", "McTest", 60000)

print(emp_1.fullname()) # The brackets are so that the methods runs.
print(Employee.fullname(emp_2)) # Another way of doing this.

# print("{} {}".format(emp_1.first, emp_1.last)) # This is used if there are no methods.

# emp_1 = Employee() # Instance of a class.
# emp_2 = Employee()

###  This method is prone to mistakes and
###  is time consuming...
# emp_1.first = "Jonathan"
# emp_1.last = "Pieczara"
# emp_1.email = "jonathan.pieczar@company.com"
# emp_1.pay = "60000"

# emp_2.first = "Test"
# emp_2.last = "McTest"
# emp_2.email = "test.mctest@company.com"
# emp_2.pay = "60000"