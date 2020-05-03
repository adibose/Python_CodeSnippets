import re


# a = (i.strip() for i in open("C:\\Users\\bshil\\Desktop\\Steps_Load_CDRFile.txt") if not i.isspace())
# try:
#     while(next(a)):
#         print(next(a))
# except StopIteration as e:
#     print("End of File")




pattern = '^([A-Za-z0-9_\-]+)@([A-Za-z0-9]+)\.([a-zA-Z]{2,3})$'

# n = int(input())
# ValidEmailList = []
# for i in range(n):
#     email = input()
#     if(re.search(pattern,email)):
#         ValidEmailList.append(email)
#
# ValidEmailList.sort()
# print(ValidEmailList)

#Using comprehension

n = int(input())
EmailList = []
for i in range(n):
    EmailList.append(input())

# ValidEmailList = [email for email in EmailList if re.search(pattern,email)]
# print(ValidEmailList)

def validEmail(email):
    if re.search(pattern,email):
        return email


#ValidEmailList = list(filter(validEmail,EmailList))
ValidEmailList = list(filter(lambda email : re.search(pattern,email),EmailList))

ValidEmailList.sort()
print(ValidEmailList)


