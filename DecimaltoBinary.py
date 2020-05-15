

# def decimalToBinary(num):
#     b=''
#     while(num>0):
#         b=str(num%2)+b
#         num = int(num/2)
#
#     return b
#
#
# print(decimalToBinary(15))

l=[1,1,1,1,1,1,1,1,1,1]

for i in range(1,5):
    l.insert(i*2,0)

print(l)

