import re
import os

# def happyElement(e,c,l):
#     sum = 0
#     for i in range(len(l)):
#         sum = sum+l[i]
#
#     if sum>c:
#         return False
#     else:
#         return True
#
#
#
#
#
#
# t = int(input())
# res=[]
# for i in range(t):
#     e,c = map(int,input().split())
#     l = list(map(int,input().split(' ',e)))
#     res.append(happyElement(e,c,l))

#
# for i in res:
#     print(i)



import math

#print(sum(range(100)))


# names = ['Avi','ava','Loki','Tara','Ashley','Beatty']
#
#
#
# print(list(filter(lambda name : name[0]=='a' or name[0]=='A',names)))
#
#
# pattern = re.compile('a-z A-Z 0-9')
#
# string = "My Name is Shiladitya Bose!!"
#
# #a = pattern.search(string)
#
# if(re.search('[a-z A-Z 0-9]','My ag@e is 27@')):
#     print("Pattern matched")

#print(a)


def compareTriplets(a, b):
    li=[]
    li.insert(0,0)
    li.insert(1,0)
    for i in range(0,len(a)):
        if a[i]>b[i]:
            li[0]+= 1
        elif b[i]>a[i]:
            li[1] += 1
        else:
            continue
    return li

if __name__ == '__main__':
    os.environ['OUTPUT_PATH'] = 'C:\\Users\\bshil\\Desktop\\Output.txt'
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()














