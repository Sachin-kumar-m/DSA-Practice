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

# To optimize sapce complexity we can go with another approach
'''
the approach is simple, we iterate through all the elements in the array,
and mark it as visited by make the number in the index as negative,

so that means any index element which is not a negative that index+1 is the missing number
'''
def optimization(nums):
    for num in nums:
        index = num - 1
        if nums[index]>0:
            nums[index] = - nums[index] #marking the element in the index as visited by making it negative
    ans = []
    for i in range(len(nums)):
        if nums[i]>0:
            ans.append(i+1)
    return ans
# TimeCompexity : O(N), we are itterating throught the array once.
# Space Compexity : O(1), we are not using extra space, 