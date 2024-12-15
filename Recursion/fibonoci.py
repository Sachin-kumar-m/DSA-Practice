


A = 7

def fib(A):
    # if A==0:
    #     return 0
    # if A==1:
    #     return 1
    if A<=1:
        return A
    return fib(A-1)+fib(A-2)
print(fib(A))