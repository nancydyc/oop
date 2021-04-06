class Employee:
    raise_amount = 0.66
    number_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + last + "@example.com"
 
    # update first name but want to update email automatically as well  
    @property
    def email(self):
        return f'{self.first}{self.last}@example.com'

    @property
    def fullname(self):
        return self.first + " " + self.last

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

emp_1 = Employee("Nancy", "Dai", 6666)

emp_1.fullname = 'Quency Luu'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

# update first name and email at the same time
emp_1.first = 'Jim'
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_2 = Employee("Wenhong", "Hu", 8888)
print(emp_2.email)
emp_2.first = 'Apple'
print(emp_2.email)

del emp_1.fullname
