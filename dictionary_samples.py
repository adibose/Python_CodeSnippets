class User:
    def __init__(self,user):
        self.fname = user.get('fname')
        self.lname = user.get('lname')
        self.email = user.get('email')
        self.dob = user.get('dob','01/01/1900')

    def findAge(self):
        if self.dob != '':
            birthYear = int(self.dob[6:10])
        else:
            birthYear = 1900
        print("{}'s age is : {}".format(self.fname,str(2019-birthYear)))
#Create user dictionary
user={}

#Assign key-values to dictionary
user['fname'] = input("Enter firstName : ")
user['lname'] = input("Enter lastName : ")
user['email'] = input("Enter email : ")
user['dob'] = input("Enter dob in DD/MM/YYYY format : ")

firstUser = User(user)
firstUser.findAge()

