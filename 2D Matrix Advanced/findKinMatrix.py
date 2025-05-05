'''
given a n*m matrix where all the elements are sorted in both column and row wise, find k
'''

'''approach:
we loog for the last elemet in each row, if it is greater then we skip that cloumn,
and same thing for column also
'''

def search(A,k):
    i = 0
    j = len(A[0])-1

    while i<len(A) and j>0:
        if A[i][j]>k:
            j+=1
        elif A[i][j]<k:
            i+=1
        else:
            return True
    
    return False

# Time Complexity : O(N+M)
#Space Complexity : O(1)