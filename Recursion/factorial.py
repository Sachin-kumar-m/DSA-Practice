'''
Find the factorial of a given number using recursion
'''

A = 2
def factorial(A):
    if A<1:
        return 1
    return factorial(A-1)*A

print(factorial(A))