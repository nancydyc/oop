import datetime

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
        self.pay = self.pay + self.raise_amount

    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

    # Using regular method for self like below, only apply to one instance, not a whole class,
    # This change won't be inherited by subclass
    # def set_raise_amt(self, amount):
    #     self.raise_amount = amount

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split("-")
        return cls(first, last, pay) # alternative constructors

    @staticmethod # Use staticemethod when not touching self or cls
    def is_worday(date):
        if date.weekday() == 5 or date.weekday() == 6:
            return False
        return True


class Developer(Employee):
    raise_amount = 1111
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def manage_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    def apply_raise(self):
        self.pay = (self.pay + self.raise_amount) * 1.5 # Override parent class apply_raise method


emp_1 = Employee("Nancy", "Dai", 6666)
print(emp_1.__dict__) # namespace for this instance
print(emp_1.email) # preperty
print("Employee 1: ", emp_1.fullname()) # method

print("====================================================================================")
# Use class variable
emp_1.apply_raise()
print("Adjust raise for emp_1: ", emp_1.pay)
emp_1.raise_amount = 0.88 # overwrite the classmethod
print("Base raise apply to all employees (Class variable) is still: ", Employee.raise_amount)
emp_1.apply_raise()
print("Adjust 2nd raise for emp_1: ", emp_1.pay)

emp_2 = Employee("Wenhong", "Hu", 8888)
print("Employee 2: ", emp_2.fullname())
print(Employee.number_of_emps)

print("====================================================================================")
# Use classmethod
print("Original base r# # aise", Employee.raise_amount)
Employee.set_raise_amt(0.99) # same as Employee.raise_amount = 0.99
print("New raise amount for all emps", Employee.raise_amount)
emp_3 = Employee("Tony", "Cai", 9999)
print("Adjust raise for new emp_3", emp_3.raise_amount)
print("Adjust 3rd raise for emp_1", emp_1.raise_amount) # raise_amount not changing because of setting by instance not class
print("Adjust raise for emp_2", emp_2.raise_amount)
emp_1.apply_raise()
emp_2.apply_raise()
emp_3.apply_raise()
print(f"Look all right, so apply raise: \nemp_1: {emp_1.pay} \
                                        \nemp_2: {emp_2.pay} \
                                        \nemp_3: {emp_3.pay}\n")
emp_str_11 = 'Jane-Dow-6000'
new_employee_11 = Employee.from_string(emp_str_11)
print("New employee 11:", new_employee_11.fullname(), new_employee_11.email, new_employee_11.pay)

print("====================================================================================\n")
# Use staticmethod
date_1 = datetime.date(2021, 4, 1) # Thr
date_2 = datetime.date(2021, 4, 4) # Sun
print("Go to work? ", Employee.is_worday(date_1))
print("Go to work? ", Employee.is_worday(date_2))

print("====================================================================================\n")
# Inheritance
dev_1 = Developer('DT', 'Wu', 88000, 'Python')
dev_2 = Developer('DJ', 'Song', 99000, 'Java')
print(dev_1.email, dev_1.prog_lang )
print(dev_2.email, dev_2.prog_lang)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

mgr_1 = Manager('Xian', 'Lee', 120000, [dev_1])
print(mgr_1.fullname(), mgr_1.email)
mgr_1.add_emp(dev_2)
mgr_1.manage_emps()
print("New report line after removing dev 1:")
mgr_1.remove_emp(dev_1)
mgr_1.manage_emps()

print(isinstance(mgr_1, Employee)) # True
print(isinstance(mgr_1, Developer)) # False
print(issubclass(Developer, Employee)) # True

print("====================================================================================\n")
# Special methods
print(repr(emp_1))
print(str(emp_1))
# same as above
print(emp_1.__repr__())
print(emp_1.__str__())

print(emp_1.__add__(emp_2))
print(emp_1.__len__())
# above and below are the same
print(emp_1 + emp_2)
print(len(emp_1))

print("========================================Override methods============================================\n")
# Override methods
emp_4 = Employee("David", "Tang", 145000)
print("Emp 4's original pay", emp_4.pay)
print(emp_4.raise_amount)
Employee.set_raise_amt(5000)
# Employee.raise_amount = 5000 # same as above
# emp_4.set_raise_amt(5000) # Only override one instance's raise_amount using regular self method intead of classmethod
print("Override class method raise_amount:", emp_4.raise_amount)
emp_4.apply_raise()
print("Emp 4's new pay", emp_4.pay)

new_manager = Manager("Buffulo", "Smith", 165000)
print("New manager's initial pay:", new_manager.pay)
print("New manager's raise:", new_manager.raise_amount)
new_manager.apply_raise()
print("New manager's new pay after overriding employee's apply_raise:", new_manager.pay)