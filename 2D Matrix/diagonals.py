'''
given a square matrix. print all the diagonal elements. from left-right and right-left
'''
A = [[4,3,1,7],[6,2,0,4],[5,3,9,7],[1,2,3,4]]

def prettyPrint(A):
    for i in A:
        print(i)

def diagonal(A): #can be done using while loop as well
    for i in range(len(A)):
        print(A[i][i], end = " ")

    #while implementation
    # i = 0
    # while i<len(A):
    #     print(A[i][i], end=" ")
    #     i+=1

def right2Left(A):
    # i = len(A)-1
    # j = 0
    # while i>=0:
    #     print(A[j][i], end=" ")
    #     i-=1
    #     j+=1
    n = len(A)
    for i in range(n):
        print(A[i][n-1-i], end = " ")


prettyPrint(A)
diagonal(A)
print()
right2Left(A)

# time Complexity: O(N),
# space complexity : O(1)