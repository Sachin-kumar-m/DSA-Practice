'''
Leetcode 217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:
Input: nums = [1,2,3,1]
Output: true
Example 2:
Input: nums = [1,2,3,4]
Output: false
Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

'''approach: we can use sets here, accessing any element in a set if O(1) time 
complexxity, also sets cannot have duplicate values, so we can add all the elements 
from our arry to our set and compare the length of sets and array,
if both are same then there are not duplicates,

'''

def solution(nums):
    number_set = set()

    for num in nums:
        number_set.add(num)
    if len(number_set)==len(nums):
        return False
    return True
A = [1,1,1,3,3,4,3,2,4,2]
print(solution(A))