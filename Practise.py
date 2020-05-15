import math


def sumOfNaturalNos(n):
    if n == 1:
        return 1
    else:
        return n + sumOfNaturalNos(n-1)

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)









print(sumOfNaturalNos(2))
print(fact(5))
