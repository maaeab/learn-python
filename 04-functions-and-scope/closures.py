# author: moemen.ahmed@gmail.com
# date: 02 May 21
# purpose: Test more with Python functions, closures and other aspects of functional programming
# The criteria that must be met to create closure in Python are summarized in the following points.
#   We must have a nested function (function inside a function).
#   The nested function must refer to a value defined in the enclosing function.
#   The enclosing function must return the nested function.

def func1():
    return "!"

def func2():
    return "@"
    
def s(a, b):
    res = ""
    for i in range (0, a):
        res += "\n"+func1()
        for j in range (0, b):
            res += func2()
    # return res
    def printResult():
        print(res)
    # in the below line we return the printResult() as a closure
    return printResult

def main():
    print("Welcome to Moemen's Lab") 
    # x = int(input("Enter X value: "))
    # y = int(input("Enter Y value: "))
    result = s(3,3)
    result()
    print(type(result))
    # print(result() + "\n")
main()