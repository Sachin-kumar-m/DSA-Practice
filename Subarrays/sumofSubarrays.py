'''
given an array of length n, find the sum of each subarray
'''

A = [6, 8 ,-1,7]


# brute Force
def sumOfSubarrays(A):
    result = []
    for i in range(len(A)): 
        for j in range(i,len(A)):
            summ = 0
            for k in range(i,j+1):
                summ+=A[k]
            result.append(summ)
    return result
# print(sumOfSubarrays(A))

# Time Complexity : O(N^3)
# Space COmplexit: O(1)
'''# optimization, here for the third loop we are just finding sum for a given range. so we can use the
prefix sum technique but we will have to compromise on space complexity
'''

def optimization(A):
    prefixArray = [0]*len(A)
    prefixArray[0] = A[0]
    for i in range(1,len(A)):
        prefixArray[i] = prefixArray[i-1]+A[i]

    for i in range(len(A)):
        for j in range(i,len(A)):
            if i==0:
                print(prefixArray[j],end=",")
            else:
              print(prefixArray[j]-prefixArray[i-1],end=",")
optimization(A)