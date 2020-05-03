A=[1,2,2,1]

A.sort()

for i in range(0,len(A)-1,2):
    A[i],A[i+1] = A[i+1],A[i]


print(A)
