# 2. Write a program which accepts a sequence of comma-separated
# numbers from console/user and generates a list and a tuple which contains every
# number.

# Moemen Ahmed, 1May2021

myList = []
i = ""
# while (i != 'x'):
#     i = input("Enter a new integer or 'x' to exit ; ")
#     if i != 'x':
#         myList.append(i)    

i = input("Enter a comma-separated list of elements: ")
myList = i.split(',')
myTupel = (myList)
print (myList)
print (myTupel)