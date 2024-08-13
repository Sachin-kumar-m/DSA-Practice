'''
Given an integer array where all the elements are not unique, we need to find the total number of nobal elements

Nobal Element : an element is said to be a nobal element when (count of elements < A[i]) = element itself

ex : [-1,1,2,3,4,5,7,8] here 4 and 5 are nobal elements since there are 4 elements that are less than 4 and 5 elements that 
are less than 5
'''

A = [-10,1,1,2,4,4,4,8,10]
def approach(A):
    if A[0]==0:
        ans = 1
    else:
        ans = 0
    
    for i in range(1,len(A)):
        if A[i-1]!=A[i]:
            count = i
        elif A[i-1]==A[i]:
            count = count
        
        if count == A[i]:
            ans+=1
    return ans
print(approach(A))