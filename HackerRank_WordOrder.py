
n = int(input())
words=[]

for i in range(n):
    words.append(input())

unique=0
count_arr=[]
check = []
for i in words:
    if words.count(i)==1:
        unique+=1
        count_arr.append(1)
    else:
        if i not in check:
            check.append(i)
            unique+=1
            count_arr.append(words.count(i))
            words.remove(i)

print(unique)
for i in count_arr:
    print(i,end=" ")




