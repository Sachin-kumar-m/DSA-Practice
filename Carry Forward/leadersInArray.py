"""
Given an array of length N, we need to find the count of leaders in an array
an element is said to be a leader if all the elements to its right are smaller than the element.
by default the right most element A[n-1]th element is always considerd as a leader
"""

"""
Approach, we can have a variable to currentLeader, and count. and my currentLearder will be A[n-1]

now i iterate from right and check if any element is greater than my currentLeader, if yes i reassign currentLeader
to the greater element that was found, and increment my count value.
"""


A = [15, -1, 7, 2, 5, 4, 2, 3]

def leaderInArray(A):
    n = len(A)
    count = 1 #initially the count is 1 since the last element is always considered as a leader
    currentLeader = A[n-1] #since last element is considered as an array, we are assigning it as the current leader
    for i in range(n-1,-1,-1):
        if A[i]>currentLeader: #if we find any greater element we are replacing the currentLeader with the new element
            currentLeader=A[i]
            count+=1
    return count

print(leaderInArray(A))

# Time Complexity : O(N), we are iterating though the array only once. 
# Space Complexity : O(1), we are using any extra space. 