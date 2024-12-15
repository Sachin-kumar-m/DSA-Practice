'''
Given A and N, find the power of A^N using recursion
'''


A = 2
N = 5

def power(a,n):
    if n==0:
        return 1
    return a*power(a,n-1)

print(power(A,N))

#another approach, we now divide A, in terms of A/2

def optimization(a,n):

    if n==0:
        return 1
    if n%2==0:
        return (optimization(a,n/2)*optimization(a,n/2))
    
    return a*(optimization(a,n//2)*optimization(a,n//2))
A = 2
N = 3
print(optimization(A,N))