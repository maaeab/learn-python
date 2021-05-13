# 1. With a given number n, write a program to generate a dictionary that
# contains (i, i*i) such that i is an number between 1 and n (both included). and
# then the program should print the dictionary.

# Moemen Ahmed - 1May2021

i = int(input("Please insert the upper limit as an integer number: "))
squares = {}
for j in range(i, 0, -1):
    squares[j] = j*j

for i,j in squares.items():
    print (f"Number: {i}, Square: {j}")