'''
given a matrix of NxM print all the diagonlas from Right-Left
'''

'''
we can break the matrix into 2 triangles. one upper triangle and one lower triangle

we can get i and j and keep incrementing i and decrementing j until i<len(A)

this is for one diagonal, to print lower triangle do the same for k times (len(A))


to print upper triangle, same approach but j value will be len(A[0])-2, sine we have to start
from 2nd last element of the first row.


print all the diagonlas starting with row 0 (top row)

then print all the diagonlas starting with m-1 col (last column)
'''

# A = [[1,2,3,4,5],[6,7,8,9,1],[1,2,3,4,5],[1,2,3,6,8]]

A = [[1,2,3,4],[5,6,7,8],[9,1,2,3],[3,4,5,6]]

for i in A:
    print(i)

def diagonal(A):
    # printing all the diagonals starting from last column. row = i, col=len(A[0])-1
    for i in range(1,len(A)):
        row = i
        col = len(A[0])-1
        while row<len(A) and col>=0:
            print(A[row][col], end=" ")
            row+=1
            col-=1
        print()
    # printing all the diagonals starting from first row, row = 0, col = i
    for i in range(len(A)):
        row = 0
        col = i
        while row<len(A) and col>=0:
            print(A[row][col], end=" ")
            row+=1
            col-=1
        print()

diagonal(A)


# Time Complexity: O(N^2), while loop will have n iterations and a for loop of n iterations
# Space Complexity: O(1), not using any extra space