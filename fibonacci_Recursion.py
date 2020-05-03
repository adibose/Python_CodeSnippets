import sys
def fib(n):
    if n == 1:
        return 1
    elif n==0:
        return 0
    else:
        return fib(n-1)+fib(n-2)


def binarySearch(items,num,lower,upper):
    mid = (lower + upper)//2
    if lower<=upper and items[mid] == num:
        print("found")
    elif lower>upper:
        print("Not found")
    elif(items[mid]>num):
        binarySearch(items,num,lower,mid-1)
    elif(items[mid]<num):
        binarySearch(items,num,mid+1,upper)
    else:
        return -1
A = [0,0]
def binary(n):
    if n<1:
        print(A)
    else:
        A[n-1] = 0
        binary(n-1)
        A[n-1] = 1
        binary(n-1)

binary(2)


binarySearch([1,2,3,4,5,6,7,8,9],10,0,8)


print(fib(10))
print(sys.getrecursionlimit())