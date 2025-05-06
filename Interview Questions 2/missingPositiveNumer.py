'''
Given an array of numbers we need to find the first missing positive integer

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
'''

# Approach 1: we can create a dictionary with all the numbers from the array and then iterate throough and check if 1 to n-1 elements
# present in the dictionay, then if its not presenet we return that value
'''
this approach take extra space but On(N) time complexity.
'''


'''
Approach 2: for every element i check if it is in its right position. for example 1 should be at 0th index
2 should be at 1st index

similarly element V-1 should be at Vth index
if we come accross any element that is greater than len of array we skip or if we come across any 
element less than 0 also we skip
else, if the elemnt is not in right index we swap to its right index
'''

'''
edge case, this code will not work if we have duplicate values.

so to fix we can have another check 

if A[i] == A[A[i]-1] then i+=1 else we swap
'''

def missingElement(A):
    i = 0
    while i<len(A):
        if A[i]>len(A) or A[i]<1:
            i+=1
        elif A[i]-1 != i:
            A[A[i]-1],A[i] = A[i],A[A[i]-1]
        
        elif A[i]-1==i:    
            i+=1
    
    #by now we have all our elements in its right place
    #so we can run a for loop to check if its not in its position then the first element out of position is our element

    for i in range(len(A)):
        if A[i]-1 !=i:
            return i+1
    return len(A)+1 #if every elemet are present in the array then the n+1 element is the missing element

nums = [1,2,0]
print(missingElement(nums))
nums = [3,4,-1,1]
print(missingElement(nums))
nums = [7,8,9,11,12]
print(missingElement(nums))