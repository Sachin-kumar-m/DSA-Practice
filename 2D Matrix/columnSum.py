'''
given a matrix of length NxM, print the column sum
'''

A = [[4,3,1,7],[6,2,3,4],[5,3,2,7]]
def prettyPrint(A):
    for i in A:
        print(i)
def columnSum(A):
    n = len(A)
    m = len(A[0])
    for i in range(m): #here we are iterating the num of rows
        result = 0
        for j in range(n): #here we are iteratin the num of colums
            result+=A[j][i] #A[j][i] because j has to increase every time..
        print(result)
prettyPrint(A)
columnSum(A)


# time Complexity: O(N*M), we are iterating through NxM matrix
# space Complexity: O(1), not using any extra space