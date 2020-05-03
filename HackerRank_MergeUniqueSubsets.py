def merge_the_tools(s, k):
    iter = int(len(s)/k)
    j=0
    a=[]
    li=list(s)
    for i in range(1,iter+1):
        a.append(li[j:(k*i)])
        j = j+k

    li=[]
    final=[]
    for i in range(0,len(a)):
        for j in a[i]:
            if(j not in li):
                li.append(j)
        final.append(li)
        li=[]
    return final

s = input()
k = int(input())

res = merge_the_tools(s,k)

for i in res:
    print(''.join(i))



