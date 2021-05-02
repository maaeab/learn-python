# 6. Write a program which can compute the given factorial of a number.
# Moemen Ahmed - 1May21

def factorial(i: int):
    if (i == 0):
        return 1
    else:
        return i * factorial(i-1)


print(factorial(5))