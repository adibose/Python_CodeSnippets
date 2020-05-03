from collections import Counter


n = int(input())

words = [input().strip() for _ in range(n)]

cnt = Counter(words)

print(len(cnt))

for word in words:
    a=cnt.pop(word,None)

    if a==None:
        continue
    else:
        print(a,end=" ")