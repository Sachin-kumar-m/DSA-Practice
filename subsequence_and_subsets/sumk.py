'''
Given N distinct elemetns, check if there exits a subset with sum = k 
'''


'''approch : map each 2^N subsets to a number from 0-2^N in bit manupilation form

ex : if there are 3 elements in the array then our bit size is 2^3 = 8

0-0-0 = do not consider any element from the array
0-0-1 = take the element which is in the 0th index
0-1-0 = take the element which is in the 1st index
0-1-1 = take elemetns which are in oth and 1st index

we can generate such pattern so we can list all our subsets in the given array.

and from that we can generate the sum of each subset and check if it is equal to K
and return True of False based on that
'''

A = [3,-2,1]


def checkSum(A,k):
    for i in range(0,2**k):
        ans = 0
        for j in range(len(A)):
            if checkBit(i,j):
                ans+= A[j]
        if ans == k:
            return True
    return False

def checkBit(i,j):
   return i and (1<<j)

print(checkSum(A,1))