''''
Trapping water problem, (LeetCode Hard 42)
iven n non-negative integers representing an elevation map where the width of each bar 
is 1, compute how much water it can trap after raining.
Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array 
[0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are
 being trapped.
'''


# approach
'''
for every element we find max left element and max right element
and then level = min(maxleft,maxright)-element
if the level is a positive integer then we add to our solution
'''

'''
to find the maxleft element we can create an array that stores all the max element
from 0,i-1
'''

def maxLeft(A):
    pf=[0]*len(A)
    pf[0]=A[0]
    for i in range(1,len(A)):
        pf[i]= max(pf[i-1],A[i-1])
    return pf

'''
to find the maxright element we can create another arry that stores all the max element
from i to n-1
'''

def maxRight(A):
    pf=[0]*len(A)
    pf[len(A)-1]=A[len(A)-1]
    for i in range(len(A)-2,-1,-1):
        pf[i]= max(pf[i+1],A[i])
    return pf

def rainWaterTrapping(A):
    leftMax = maxLeft(A)
    rightMax = maxRight(A)
    solution = 0
    for i in range(len(A)):
        level = min(leftMax[i],rightMax[i])-A[i]
        if level>0:
            solution+=level
    return solution

A = [0,1,0,2,1,0,1,3,2,1,2,1]
print(rainWaterTrapping(A))

# Time Complexity: O(N), in maxLeft function we do O(N), same with maxRight function and rainwater function also
#O(N)+O(N)+O(N) = O(N)

# Space Complexity: O(N) = O(N)+O(N), one array in rightMax funtion and one in maxleft function