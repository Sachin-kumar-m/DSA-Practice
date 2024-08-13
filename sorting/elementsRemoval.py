'''
Given an integer array, at every step remove an element from the array
cost to remove an element = sum of all the remaining elements in the array
find the minimum cost to remove all the elements from the array
'''

'''
approach: sort the given array and remove the highest elements from the list, so that 
when the highest value element is removed the sum becomes less

contribution of A[i] to minimum cost = A[i]*(Number of time it appears in the sum)
'''

A =[3,6,2,4]
# A =[2,3,4,6]
def approach(A):
    A.sort()
    ans = 0
    temp = 1
    for i in range(len(A)-1,-1,-1):
        ans = ans + (A[i]*temp)
        temp+=1
        A.pop()
    return ans
print(approach(A))

# TC : O(NLogN + N )= O(nLogn), since we are sorting so nLogn
# SC : O(1)
