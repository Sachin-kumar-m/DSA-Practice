'''
Given N distinct elements find the sum of subset sums
'''



def subsetSums(A):
    ans = 0
    for i in range(2*len(A)):
        count = 0
        for j in range(len(A)):
            if countBit(i,j):
                count+= A[j]
        ans +=count
    return ans

def countBit(i,j):
    return i and (1<<j)

A = [3,1,4]

print(subsetSums(A))

'''
another idea is to use contribution technique. meaning. we can get how amy times each elemes contributes to the total answer,

then we can multiply the value with number of times it appears, 

and for a subset every elemet appears 2^n-1 times
'''

def optimization(A):
    n = len(A)
    ans = 0
    for i in range(n):
        ans += A[i]*(2**(n-1))
    return ans

print(optimization(A))

# TC : O(2^N * N)
# SC : O(1)