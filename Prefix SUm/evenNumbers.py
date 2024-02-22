
"""
this is another variation to find the even/odd numbers in the given set of ranges.

You are given an array A of length N and Q queries given by the 2D array B of size Q×2.

Each query consists of two integers B[i][0] and B[i][1].
For every query, your task is to find the count of even numbers in the range from A[B[i][0]] to A[B[i][1]].


Explain: to get a solution to this one, we can iterate through the given array and if the index has 
an even number we increment our number and form a prefix array. at any given index of the prefix array
it will give the count of even/odd numbers from 0 to ith index. so to get the even number in the range 
we can use ans[i] = pf[r]-pf[l-1]
"""


A = [2, 1, 8, 3, 9, 6]
B = [[0, 3],[3, 5],[1, 3],[2, 4]]  #list of query with ranges


def evenNumbersInRange(A,Q):
    pf = [0]*len(A)
    if A[0]%2==0:   #checking if the first element is even, if yes then pf[0] will be 1 else 0
        pf[0]=1
    
    for i in range(1,len(A)):
        if A[i]%2==0:
            pf[i]=pf[i-1]+1
        else:
            pf[i]= pf[i-1]

    ans = [0]*len(Q)

    for i in range(len(Q)):
        l = Q[i][0]
        r = Q[i][1]
        if l==0:
            ans[i] = pf[r]
        else:
            ans[i] = pf[r]-pf[l-1] #this is same as prefix sum formula.
    return ans

print(evenNumbersInRange(A,B))

"""
Time complexity: O(N+Q), since we are iterating through the given array and also the Q queries
Space Complexity: O(N), we are creating a new array of length N
"""
    

