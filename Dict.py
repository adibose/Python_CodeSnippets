student = {'name':'John','age':25,'courses':['Math','CS']}

#To display each item separately
for key in student:# todo practise
    print(key, student[key])

for key,value in student.items():
    print(key,value)

#print(student['mobile'])-- will throw error as mobile key is not there

#Use get function in order to avoid key error and also to assign a default value if key does not exist

print(student.get('mobile','Not Found')) #will print Not Found as key mobile is missing

student['name']= 'Jack'

print(student)

#if you want to update many values in the dictionary then use update

student.update({'name':'Mohan','age':27})
print(student)

#remove elements using del

del student['age']
print(student)
