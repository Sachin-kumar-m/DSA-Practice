'''
given an array of length n, find the maximum subarray sum of length k

approach: we can have an initails window size of k and then find the sum and find sum of the subarray and keep tracking the max sum
'''

#brute force
A = [-3,4,-2,5,3,-2,8,2,-1,4]
k = 5

def maxSubarray(A,k):
    s = 0
    e = k-1
    ans = -float('inf')
    while e<len(A):
        val = 0
        for i in range(s,e+1):
            val+=A[i]
        ans = max(ans, val)
        s+=1
        e+=1
    return ans
print(maxSubarray(A,k))

# time complexity: O((N-k+1)*k), this can be further reduced to O(N^2)
# space complexity: O(1), we are not using extra space

''' optimization : in the inner loop we are trying to find the sum in a given range. so we can use prefix sum. but we will have to
compromise on the space.
'''

def prefixSumApproac(A,k):
    prefixSum = [0]*len(A)
    prefixSum[0] = A[0]
    for i in range(1,len(A)):
        prefixSum[i] = prefixSum[i-1]+A[i]
    result = 0
    s = 0
    e = k-1
    while e<len(A):
        value = 0
        value = prefixSum[e]-prefixSum[s-1]
        result = max(result,value)
        s+=1
        e+=1
    return result
print(prefixSumApproac(A,k))

# time complexity: o(N), to find the sum we are using constant time so the inner loop is not required. 
# space complexity: O(N), we are creating a prefix array of length N


'''Sliding Window Technique

when we are moving from one sub array to another sub array we are calculating the sum again and again. 

so currrent sum is equal to previous sum - A[s-1] + A[e+1]
we are subtracting the first element in the previous sub array and adding the next element of the new subarray
'''

def slidingWindow(A,k):
    s = 0
    e = k-1
    ans = 0
    for i in range(s,e):
        ans+=A[i]
    
    s+=1
    e+=1
    while e<len(A)-1:
        val = ans-A[s-1]+A[e+1]
        ans = max(ans, val)
        e+=1
        s+=1
    return ans

print(slidingWindow(A,k))