def pickingNumbers(a):
    # Write your code here
    s = set(a)
    ul = list(s)

    ul.sort()
    print(ul)
    maximum = 0
    if(len(ul)==1):
        maximum = len(a)
    if 0 in ul and 1 in ul and -1 in ul:
        maximum = a.count(-1) + a.count(0) + a.count(1)

    for i in ul:
        maximum=max(a.count(i),maximum)

    for i in range(0,len(ul)-1):
        if (ul[i] - ul[i + 1] == 1 or ul[i] - ul[i + 1] == -1):
            current = a.count(ul[i]) + a.count(ul[i + 1])
            maximum = max(current, maximum)

    return maximum



print(pickingNumbers([4,97,5,97,97,4,97,4,97,97,97,97,4,4,5,5,97,5,97,99,4,97,5,97,97,97,5,5,97,4,5,97,97,5,97,4,97,5,4,4,97,5,5,5,4,97,97,4,97,5,4,4,97,97,97,5,5,97,4,97,97,5,4,97,97,4,97,97,97,5,4,4,97,4,4,97,5,97,97,97,97,4,97,5,97,5,4,97,4,5,97,97,5,97,5,97,5,97,97,97]))