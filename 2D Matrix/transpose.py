'''
given a martix print the transpose of the 2D matrix

Transpose: Transfer all rows to columns, and all columns to rows

here we just swap either the lower triangle with upper , or upper triangle with lower and then we get the transpose

if the matrix is a retangular matrix, then we need to use extra space and create a new matrix to store the transpose
'''

A = [[1,2,3,4,5],[6,7,8,9,0],[0,9,8,7,1],[1,3,5,6,7],[1,1,1,1,1]]

for i in A:
    print(i)

def transpose(A):
    for i in range(len(A)):
        for j in range(i,len(A)):
            A[i][j],A[j][i] =A[j][i],A[i][j]
    return A
print()
b = transpose(A)
for i in b:
    print(i)