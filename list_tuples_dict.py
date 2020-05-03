#This is a list
subjects = ['Maths','Bio','Chem','Physics','Comp','English']

#Find the last element in the list
print(subjects[-1])
#print(subjects[len(subjects)-1])

#Find first 3 elements in the list
print(subjects[0:3])

#Find last 2 elements in the list
print(subjects[-2:])

#use extend to insert elements of list 2 in list 1
new_subjects = ['Geo','History','Bengali']
#subjects.insert(0,new_subjects) -->Can't be used as it will insert the list 2 as a group in the first index of list 1
#subjects.append(new_subjects) --> Will insert at the last as a group
subjects.extend(new_subjects)
print(subjects)
subjects.reverse()# this will alter the original list
print(subjects)
#subjects.sort()# this will alter the original list
#print(subjects)

#if you dont want to alter the original list but still want to sort the list then use 'Sorted'
print(sorted(subjects))
print(subjects.index('Maths'))
print('Sex' in subjects)

#using Enumerate to display list contents
for index,sub in enumerate(subjects,start=1):
    print(index,sub)

#list to string -- Use join

sub_str = " - ".join(subjects)
print(sub_str);


#string to list -- Use split

li = sub_str.split(' - ')
print(li)

#Example of mutabitlity of lists
l1 = [1,2,3]
l2 = l1
l1[0]=4;
print(l2)

#<----------------------Sets------------------->
#Set is an unordered,unique group of elements.

s1 = {1,1,2,3,7,6}
s2 = {1,9,5,3}

print(s1.intersection(s2))

a = [0,1,2,3,4,5,6,7,8,9]

print