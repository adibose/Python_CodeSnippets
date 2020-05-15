import math

Primes = []
for i in range(101):
    Primes.append(1)

Primes[0]=0
Primes[1]=0



for i in range(2,int(math.sqrt(100))):
    if Primes[i]==1:
        j=2
        while(i*j<=100):
            Primes.insert(i*j,0)
            j+=1

print(Primes)

