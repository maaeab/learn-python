sum = 0
multi = 0
fixedBase = 1000
def add(a, b):
    # the function can read the values of the global variables
    # the function cannot change the values of the global variables directly.
    # the below line creates a local varibale "sum"
    sum = fixedBase + a + b
    # still we can access to write to the global 'multi' variable by using the keyword global
    global multi
    multi = a * b
    # returning the local variable "sum"
    return 

# updating the global variable sum with the return of the function
add(4, 5)
print("sum : " + str(sum))
print("multi : " + str(multi))

