'''
given a 2D matrix return all the boundary elements
'''

A = [[1,2,3],[4,5,6],[7,8,9]]
for i in A:
    print(i)
        

def boundary(A):
    ans = []
    i = 0
    j = 0
    n = len(A)
    for k in range(1,n):
        ans.append(A[i][j])
        j+=1
    for k in range(1,n):
        ans.append(A[i][j])
        i+=1
    for k in range(1,n):
        ans.append(A[i][j])
        j-=1
    for k in range(1,n):
        ans.append(A[i][j])
        i-=1
    return ans
print(boundary(A))