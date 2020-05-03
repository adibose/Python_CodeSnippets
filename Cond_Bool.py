l1=[1,2,3]
l2=[1,2,3]# l2 is pointing to a different object, thatsy id is different
l3=l1# l3 and l1 are pointing to the same object

print(l1==l2)
print(l1 is l2)
print(l3 is l1)
print(id(l1))
print(id(l2))
print(id(l3))


#False values:
# 1. False
# 2. None
# 3. Zero of any numeric type
# 4. Empty string,list,dictionary

i = 0.1

if ():
    print(True)
else:
    print(False)