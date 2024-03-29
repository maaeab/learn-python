############ Numbers can be int, long, float or complex
x = 5
y = 7.0
yy = 7_000_999
z = 3+2j
i,j = 0,10
print ("This is an integer x: ", x)
print ("This is a float y: ", y)
print ("This is another flost yy: ", yy)
print (f"This is a complex z : {z}")
print (f"This is a integers i: {i}, and j: {j}")


############ Strings
myStr = "My name is Moemen Ahmed, I just love coding!"
print("Name: " + myStr[11:23])
print(myStr[-19:])
print(f"{myStr}") 

############ Lists -- lists are arrays in other languages
myList1 = [1, 2, 3]
print("This is the first element in my integer list: " + str(myList1[0]))

myStrs = ["Michael", "John", "Graham"]
print("This is the second name in my strings list: " , myStrs[1])
print(f"This is the last name in my strings list: {myStrs[2]}")


#myCombinedList = myStr + myList1 /// error of course

for i in range(0, 2):
    print (myStrs[i])
    
for i in range(0, 6):
    print ("moemen"[i])    
# strangely this works okay !! this shows that strings are list of characters.



########### Tuples: tuples are read-only lists in some way
myTuple1 = (1, 2, 'Ali', 'John', 5+3j)
print (myTuple1)
#myTuple1[0] = 1  // this shall cause an error of course
print(f"The first element of myTuple1 is: {myTuple1[0]}")



########### Dictionaries: Key, Values pairs
myDict = {'name':'mohsen', 'age':30, 'job':'teacher'}
print(f"The value of the age key in myDict is: {myDict['age']}")
print(f"Those are the keys in myDict: {myDict.keys()}")
print(f"Those are the values in myDict: {myDict.values()}")


########### Conversion bewteen data types / Casting
# notice that multiple variables initialization is accepted in python
a, b, c = 5, 6, 7
x, y, z = 0.5, 0.6, 0.7
res1 = a / x
res2 = b + y
res3 = c * z

print(f"res1: {res1}, res2: {res2}, res3: {res3}")
f = float(1000)
print(f"float(1000): {f}")

########### I can create a dictionary using paris of Key/Values in Tuples
# notice the parentheses in the below line
dict1 = dict((('h',5), ('w',10), ('l',40)))
print(f"my box sizes are: {dict1.values()}")

########### we can rewrite in a more clear way as below
t1 = (('h',5), ('w',10), ('l',40))
dict1 = dict(t1)
print(f"dict1 keys: {dict1.keys()}")

########### and we can swap values for keys in the dict created from the tuple
dict2 = dict((y, x) for x,y in t1) 
print(f"dict2 keys:  {dict2.keys()}")

########### convert a string to a list
s1 = "Hello Mr. Smith!"
list1 = list(s1)
print(f"list1 from s1 read: {list1}")
# and a list to a string
s2 = ""
# ..... using the join() function
s2 = s2.join(list1)
print(f"s2 from list1 read: {s2}")
# ..... or by imlpementing a simple loop
s3 = ""
for c in list1:
    s3 += c
print(f"s3 from list1 read: {s3}")


############ Sets
set1 = {1,2,1,2,3,4,5}
print(f"set1 : {set1}")
        
# notice below that the keyword set is used to convert other data types
set2 = set(list1)
print(f"set2 from list1 : {set2}")

# notice below that the internal parentheses are necessary to denote a tuple
set3 = set((1,2,1,2,3,4,5))
print(f"set3 from a tuple: {set3}")

# converting a dict to a set - notice that keys are graped automatically
set4 = set({"a":1, "b":2, "c":3, "d":2})
print(f"set4 from a dictionary: {set4}")

# converting a dict.values() to a set 
set5 = set({"a":1, "b":2, "c":3, "d":2}.values())
print(f"set4 from a dictionary: {set5}")


