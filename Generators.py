import random
import time

names = ["Aditya", "Arif", "Arnab", "Arko", "Riddhi", "Pallabi", "Sunny", "Pamela", "Monica"]
majors = ["Maths", "English", "Computer Science", "History"]


def people_list(num_people):
    # result=[]
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }

        yield person


t1 = time.time()
student = people_list(1000000)

for i in student:
    print(i)
t2 = time.time()

print("Time Difference : ",t2 - t1)
