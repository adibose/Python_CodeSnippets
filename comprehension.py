l = [1,2,3,4,5,6,7,8,9]

#list Comprehensions
l1 = [n*n for n in l]
print(l1)

#print all the even numbers from l using list comprehension
l2 = [n for n in l if n%2==0]
print(l2)

#letter,num pair for each letter in 'abcd' and each no. in '0123'
l3 = [(letter,num) for letter in 'abcd' for num in range(0,4)]
print(l3)

students = ["Rids","Abhishek","Aditya","Arnab"]
houses = ["Green","Red","Yellow","Blue"]

#dict comprehension
my_dict = {student:house for student,house in zip(students,houses) if student!="Rids"}
print(my_dict)

nums = [1,1,1,2,2,3,3,3,3,3,4,5,6,6,6,7,8,8,9]


my_set = {n for n in nums}
print(my_set)




