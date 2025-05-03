'''
find the subarray with maximum sum
'''


'''
Brute Force:
find all the subarrays and then get the maxsum

this is O(N^2) solution, refer Subarrays/sumofSubarrays.py
'''



'''
approach:
we can have a running sum, and keep comparining and updating the max value of ans
max(ans,runningSum)

if runningSum<0 then we reset the runningSUm to 0
'''

def maxSubarraySum(A):
    ans = A[0]
    runningSum = 0
    for i in range(len(A)):
        runningSum+=A[i]
        ans = max(ans,runningSum)
        if runningSum<0:
            runningSum = 0
        
    return ans 

# Time Complexity: O(N)
# Space Complexity : O(1)