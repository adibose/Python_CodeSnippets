class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    @property
    def fullName(self):
        return "{} {}".format(self.first,self.last)

    @fullName.setter
    def fullName(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last = last

    @fullName.deleter
    def fullName(self):
        print("Name deleted")
        self.first = ""
        self.last = ""

    @property
    def email(self):
        return "{}.{}@company.com".format(self.first,self.last)


e1 = Employee('Corey','Schafer')

e1.fullName = "Sam Schafer"
del e1.fullName
print(e1.fullName)
print(e1.first)
print(e1.last)
print(e1.email)#Since a property decorator is used, i dont have to give ().







print(arr)



