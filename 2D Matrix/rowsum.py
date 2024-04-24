'''
given a matrix of length NxM, find the row wise sum
'''
A = [[4,3,1,7],[6,2,3,4],[5,3,2,7]]

def prettyPrint(A):
    for i in A:
        print(i)

def rowSum(A):
    n = len(A)
    m = len(A[0])

    for i in range(n):
        result = 0
        for j in range(m):
            result+=A[i][j]
        print(result)

rowSum(A)

# time Complexity: O(N*M), we are iterating through NxM matrix
# space Complexity: O(1), not using any extra space