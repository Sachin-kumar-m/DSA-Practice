'''
Given an array of length N with all 0 as elements, and query set Q, return the final array with adding numbers from query (i,x) where you add x
from ith index to n-1th index for each query

exapmle:
A = [0,0,0,0,0,0,0]
q = [(1,3),(4,-2),(3,1)]

now, from q1, 3 needs be added to all the elements from 1st index to the last index
q2, -2 needs to be added from 4th index to all the remaining indicies
q3, 1 needs to be added from 3rd index to all the remaning indices. 

resulting array will be [0, 3, 3, 4, 2, 2, 2]
'''

# idea 1, for each query iterate and add through all the values (Brute Force)

A = [0,0,0,0,0,0,0]
q = [(1,3),(4,-2),(3,1)]
def answer(A,q):
    for i in q:
        for j in range(i[0],len(A)):
            A[j]+= i[1]
    return A
#Time Complexity : O(N*Q)
#Space Complexity : O(1)


'''
optimization, the question is asking us to find sum for given set of queries. so we can directly use 
prefix sum technique

here we just create a prefix array and add the value from each query to only xth index
and the we can calculate the prefix sum to get our final answer
'''
A = [0,0,0,0,0,0,0]
q = [(2,6),(0,-1),(3,2),(5,4)]
def optimization(A,k):
    for i in q:
        A[i[0]] += i[1]
    pf = [0]*len(A) #out prefix array
    pf[0] = A[0]
    for i in range(1,len(A)):
        pf[i] = pf[i-1]+A[i]
    return pf

#Time Complexity: O(N+Q)
#Space Complexity : O(N), since we are creating a new prefix array of length N. we can optimize space by utilizing the same given array
print(optimization(A,q))