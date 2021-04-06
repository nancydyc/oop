class Employee:
    raise_amount = 0.66
    number_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + "@example.com"
        
        Employee.number_of_emps += 1 
        # not using self because we don't have use case wanting to change the number based on each employee
        
    def fullname(self):
        return self.first + " " + self.last

    def apply_raise(self):
        return self.pay + self.raise_amount

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split("-")
        return cls(first, last, pay) # alternative constructors

emp_1 = Employee("Nancy", "Dai", 6666)
print(emp_1.__dict__) # namespace for this instance
print(emp_1.email) # preperty
print("Employee 1: ", emp_1.fullname()) # method

print("====================================================================================")
# use class variable
print("Adjust raise for emp_1: ", emp_1.apply_raise())
emp_1.raise_amount = 0.88 # overwrite the classmethod
print("Base raise apply to all employees (Class variable) is still: ", Employee.raise_amount)
print("Adjust 2nd raise for emp_1: ", emp_1.apply_raise())

emp_2 = Employee("Wenhong", "Hu", 8888)
print("Employee 2: ", emp_2.fullname())
print(Employee.number_of_emps)

print("====================================================================================")
# use classmethod
print("Original base raise", Employee.raise_amount)
Employee.set_raise_amt(0.99)
print("New raise amount for all emps", Employee.raise_amount)
emp_3 = Employee("Tony", "Cai", 9999)
print("Adjust raise for new emp_3", emp_3.raise_amount)
print("Adjust 3rd raise for emp_1", emp_1.raise_amount) # not changing because of setting by instance not class
print("Adjust raise for emp_2", emp_2.raise_amount)
print(f"Look all right, so apply raise: \nemp_1: {emp_1.apply_raise()} \
                                        \nemp_2: {emp_2.apply_raise()} \
                                        \nemp_3: {emp_3.apply_raise()}\n")
emp_str_11 = 'Jane-Dow-6000'
new_employee_11 = Employee.from_string(emp_str_11)
print("New employee 11:", new_employee_11.fullname(), new_employee_11.email, new_employee_11.pay)