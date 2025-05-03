'''
Given an array of length N with all 0 as elements, and query set Q, return the final array with adding numbers from query (i,x) where you add x
from ith index to jth index for each query

exapmle:
A = [0,0,0,0,0,0,0]
q = [(1,3),(4,-2),(3,1)]

now, from q1, 3 needs be added to all the elements from 1st index to the last index
q2, -2 needs to be added from 4th index to all the remaining indicies
q3, 1 needs to be added from 3rd index to all the remaning indices. 

resulting array will be [0, 3, 3, 4, 2, 2, 2]
'''

'''
optimization, similar to prefixsum problem, now instead of just adding the  value in ith index,
we will be adding -value in j+1st index. and then we can calculate the prefix sum arry to get
our final answer.
'''
def optimization(A,q):
    for i in q:
        A[i[0]]+=i[2]
        if i[1]<len(A):
            A[i[1]+1]-=i[2]
    
    pf = [0]*len(A)
    pf[0]=A[0]
    for i in range(1,len(A)):
        pf[i]=pf[i-1]+A[i]
    return pf
A = [0,0,0,0,0,0,0]
q = [(1,3,2),(2,5,3),(2,4,-1)]
print(optimization(A,q))

#Time Complexity: O(N+Q)
#Space Complexity : O(N), since we are creating a new prefix array of length N. we can optimize space by utilizing the same given array
