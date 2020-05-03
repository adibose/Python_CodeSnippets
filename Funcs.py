import factorial
import calendar
import datetime
import os
import sys
import random
def hellofunction(greeting,name = 'You'):
    return "{}, {}!! ".format(greeting,name)

print(hellofunction('Hello','Sunny'))
print(hellofunction('Hello'))


courses = ['Devops','Java','Python','Hadoop','Golang','React']

random_course = random.choice(courses)

print(random_course)

print(factorial.fact(7))

print(datetime.datetime.today())
print(calendar.isleap(2020))
print(os.getcwd())

print(min(1,3,7,0,-3))

#Enclosing scope

def outer():
    x = "Outer x"
    def inner():
        nonlocal x #in order to access the outer method variable we use nonlocal keyword. We can't use global keyword here
        x = "Inner x"
        print(x)
    inner()
    print(x)

outer()