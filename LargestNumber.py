from functools import cmp_to_key

A = [0,0,0,0,0]

A = map(str,A)

key = cmp_to_key(lambda x,y: 1 if x+y>=y+x else -1)

res = ''.join(sorted(A,key = key, reverse = True))

print(res)

res = res.lstrip('0')

print(res)

if res:
    print(res)
else:
    print(0)