'''
given an integer array of length n, and subarray length B, we need to return the starting index of the subarray which has the 
minimum average

return the starting index of the subarray with smallest average
'''

'''
Approach: we can use sliding window technique. where we keep calculating the subarray sum, the sub array with smallest 
sum will have smallest average. when ever we find the smallest sum subarray, we update the index also the min_sum
'''

# A = [15,3,15,6,9,14,8,10,9,17]
# B = 1

A = [3, 7, 90, 20, 10, 50, 40]
B = 3

def smallestAverage(A,B):
    current_sum = 0
    for i in range(B):
        current_sum+=A[i]
    startIndex = 1
    endIndex = B
    min_sum = current_sum
    ans = 0
    while endIndex<len(A):
        current_sum = current_sum - A[startIndex-1]+ A[endIndex]
        if current_sum<min_sum:
            ans = startIndex
            min_sum = current_sum
        startIndex +=1
        endIndex +=1
    return ans

print(smallestAverage(A,B))

# Time Complexity : O(N) we are iterating through all the elements in the array
# Space Complexity: O(1), we are not using extra space
