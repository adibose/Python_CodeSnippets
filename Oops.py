class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullName(self):
        return "{} {}".format(self.first, self.last)

    def applyRaise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __len__(self):
        return len(self.fullName())

    #to provide meaningful output when trying to print an object
    def __str__(self):
        return "{} - {}".format(self.fullName(),self.email)

class Developer(Employee):
    raise_amount = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self,emp):
        if emp not in self.employees:
            self.employees.remove(emp)

    def print_emp_under_manager(self):
        for emp in self.employees:
            print('-->',emp.fullName())



d1 = Developer("Harry","Huang",50000,"Javacript")
d2 = Developer("Nanditha","Pamal",45000,'Scala')
d3 = Developer("Shiladitya","Bose",65000,'Python')

m1 = Manager("Guru","Prasad",80000,[])

m1.print_emp_under_manager()
m1.add_employee(d1)
m1.add_employee(d2)

m1.print_emp_under_manager()

print(d3)
print(len(m1))

#dunder methods

print(int.__add__(2,3))
print(str.__add__('2','3'))

