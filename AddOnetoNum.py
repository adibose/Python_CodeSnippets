import sys

A=[1,2,3,0,0,0]
s=''
res = []
for i in A:
    s = s+ str(i)


AddOne = int(s)+ 1
for i in str(AddOne):
    res.append((int(i)))

print(res)




