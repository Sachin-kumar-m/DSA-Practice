'''
given an array print all the subarrays
'''

A = [6,8,-1,7]

def printSubarray(A):
    for i in range(len(A)):
        for j in range(i,len(A)):
            for k in range(i,j+1):
                print(A[k],end=" ")
            print()
    
printSubarray(A)

# Time Complexity : O(N^3) since we are iterating through the array 3 times
# Space Complexity : O(1), we are not using any extra space