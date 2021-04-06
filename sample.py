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

emp_1 = Employee("Nancy", "Dai", 6666)
print(emp_1.__dict__) # namespace for this instance
print(emp_1.email) # preperty
print("Employee 1: ", emp_1.fullname()) # method

print("====================================================================================")
# use class variable
print("Adjust raise 1: ", emp_1.apply_raise())
emp_1.raise_amount = 0.6666
print("Base raise apply to all employees (Class variable) is still: ", Employee.raise_amount)
print("Adjust raise 2 for emp_1: ", emp_1.apply_raise())

emp_2 = Employee("Wenhong", "Hu", 8888)
print("Employee 2: ", emp_2.fullname())
print(Employee.number_of_emps)