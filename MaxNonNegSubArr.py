a = [1,1,-1,0,2]
li=[]
resLi=[]
sum=0
maximum=0
for i in a:
    if i>=0:
        li.append(i)
        sum+=i
    else:
        if maximum <= sum:
            maximum=sum
            resLi=list(li)
        li=[]
        sum=0

if maximum < sum:
    maximum=sum
    resLi = list(li)

print(resLi)


