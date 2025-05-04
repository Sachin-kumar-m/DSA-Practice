'''
given a 2D matrix of length N*M, and Q queries. we need to find the sum of the submatrix
for each query
each query will have x,y coordinates. 


approach. any query sum problem we have to use prefix summ approach.

so we can have a new matrix where we calculate prefix sum of rows and then prefix sum of
the columns.  
now in the new prefix sum matrix, at coordinate in the matrix gives us the 
total sum from 0,0 to that coordinate

finally to get the sum of given submatrix we can have a generalized formula

Sum = PF[x2,y2] - PF[x1-1,y2] - PF[x2,y1-1] + PF[x1-1,y1-1]

how we arrive at this formula is, at the given index it gives th sum from 0,0 to that index
but we need sum of submatrix. so we subtract the submatrices that are not required from the total sumbatrix
'''

mat = [[7,2,1,0,3],[3,1,2,3,9],[6,3,2,4,1],[3,1,2,1,4],[2,-1,6,2,3],[-1,3,2,1,4]]
q = [[2,1,4,3],[3,2,5,4]]

for i in mat:
    print(i)
    
def sumSubMatric(mat,q):
    # step1: create a prefix array
    pf = []
    for i in range(len(mat)):
        a = [0]*len(mat[0])
        pf.append(a)
    for i in range(len(mat)): #filling the first row logic pf[0]= A[0] logic
        pf[i][0] = mat[i][0]
    # step 2: create a prefix array for each row
    
    for i in range(len(mat)):
        for j in range(1,len(mat[0])):
            pf[i][j] = pf[i][j-1] + mat[i][j]
    # step 3 : create a prefix array for each column
    for i in range(0,len(mat[0])):
        for j in range(1,len(mat)):
            pf[j][i] += pf[j-1][i]
    
    # step 4: iterate though the given query set and apply formula to get the submatrix sum
    ans = [0]*len(q)
    for i in range(len(q)):
        x1 = q[i][0]
        y1 = q[i][1]
        x2 = q[i][2]
        y2 = q[i][3]

        ans[i] = pf[x2][y2] - pf[x1-1][y2] - pf[x2][y1-1] + pf[x1-1][y1-1]

    return ans

b = sumSubMatric(mat,q)
(print())
for i in b:
    print(i)

# Time Complexity : O(N*M)+O(Q)
#Space Complexity : O(N*M)