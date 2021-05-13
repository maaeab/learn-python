# 3. Write a program which will find all the numbers which are divisible by
# 7 but are not a multiple of 5, between 1000 and 1500 (both included). The
# numbers obtained should be printed in a comma-separated sequence on a single
# line.

# Moemen Ahmed - 1May2021
print("List of numbers that are divisible by 7, but not by 5, in the range (1000, 1500)")
for i in range(1000, 1501):
    if (i%7 == 0) and not (i%5 == 0):
        print(i, end = ",")
print ()


# we could have used a list myList and then convert it to a comma-separated string using ','.join(myList)