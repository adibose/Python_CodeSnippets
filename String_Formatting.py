greet = "       Hello         "
name = "Sunny"

print(greet.rstrip()+" Adi")
print(name.count('n'))
print(round(3.75,1))

#message = greet+", "+name+". Welcome!!"

# format method is used instead of + to make it more readable
message = "{}, {}. Welcome!!".format(greet,name)

# another way is using f at the beginning which is only available from Python 3.5 and above
new_message = f"{greet}, {name}. Welcome!!"

#print(help(str));

#print(new_message)