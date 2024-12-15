'''
given A,N and M, we need to find (A^N)%M
'''


A = 2
N = 10
M = 3


def fastExponents(a,n,m):
    if n == 0:
        return 1
    p = fastExponents(a,n//2,m)
    if n%2==0:
        return (p*p)%a
    else:
        return ((p*p)%m*a)%m