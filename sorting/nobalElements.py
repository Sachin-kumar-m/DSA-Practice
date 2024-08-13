'''
Given an integer array where all the elements are unique, we need to find the total number of nobal elements

Nobal Element : an element is said to be a nobal element when (count of elements < A[i]) = element itself

ex : [-1,1,2,3,4,5,7,8] here 4 and 5 are nobal elements since there are 4 elements that are less than 4 and 5 elements that 
are less than 5
'''



'''
Approach : sort the array and go through the array and find if A[i]==i then thats the Nobal element
'''
A = [-1,-5,3,5,-10,4]
A = [-3,0,2,5]
A = [-10,-5,1,3,4,5,10]
def nobalElements(A):
    A.sort()
    ans = 0
    for i in range(len(A)):
        if A[i]==i:
            ans+=1
        
    return ans

print(nobalElements(A))

# TC : nLogn + N = O(nLogn), since we are sorting
# SC : O(1)