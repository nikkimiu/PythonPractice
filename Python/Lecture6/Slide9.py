import random
first_name = input ("Enter Name: ")
length=len(first_name)
r=random.randint(0,length-1)
name=first_name[:r]+first_name[r+1:]
print(name)
