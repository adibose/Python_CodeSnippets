import math

def isPrime(num):
    for i in range(2,int(math.sqrt(num))+1):
        if(num%i==0):
            return False

    return True

def sumOfTwoPrime(n):
    if isPrime(n) or n==1 or n==0:
        return 0
    else:
        for i in range(2,(int(n/2)+1)):
            if isPrime(i):
                for j in range(n-1,(int(n/2)-1),-1):
                    if isPrime(j):
                        if(i+j==n):
                            return [i,j]
                            break


print(sumOfTwoPrime(54))