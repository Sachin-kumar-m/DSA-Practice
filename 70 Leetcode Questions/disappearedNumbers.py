'''
Leetcode 448. Find All Numbers Disappeared in an Array  
Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
You must write an algorithm that runs in O(n) time and uses O(1) extra space.
Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:
Input: nums = [1,1]
Output: [2]
Example 3:
Input: nums = [1,2]
Output: []
Example 4:
Input: nums = [1,2,3,4,5,6,7,8,9,10]
Output: []
'''


'''
Approach 1 : we can use sets here, to store all the nonduplicate values in the array

then we can have another loop from 1 to n+1 becuase 0 is not present in the given array
and also we need to check if nth value is present so we iterate till n+1 because range goes n-1th
'''

def approach(nums):
    numberSet = set()
    for i in nums:
        numberSet.add(i)
    ans = []
    for i in range(1,len(nums)+1):
        if i not in numberSet:
            ans.append(i)
    return ans
# TimeCompexity : O(N), we are itterating throught the array once.
# Space Compexity : O(n), we are using a set of worse case length N