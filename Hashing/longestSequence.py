'''
given array of length n, find the length of the longest sequence in the form (x,x+1,x+2...x+i)
with these elements appearing in any order, index of the elements does not have to be continous
'''

# approach 1: we can sort the given array and keep checking if we have continous elements


def appraoch(A):
    A.sort()

    ans = 1
    temp = 1
    for i in range(len(A)-1):
        
        if A[i] == A[i+1]:
            temp+=0
        elif A[i]+1 == A[i+1]:
            temp+=1
        else:
            temp = 1
        ans = max(ans,temp)

    return ans

A = [3,8,2,1,9,6,5,6,7,2,11,12,13,10]

A = [-1,2,3,4,5,8,9,10,11,12,13]

print(appraoch(A))

#time Complexity : O(nlog(n)) because we are sorting the array
# Space Complexity : O(1), we are not using any extra space 

        
