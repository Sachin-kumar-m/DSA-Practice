'''
given a 2D matrix print all the elements in a spiral format or also know as spiral traversal
'''

'''Approach: we can print all the boundary elements and then after that we need to increment our i,j and decrease our n by 2 (n-2)

and then again do the boundary printing. do this until our initial value < n (breaking condition)
'''

A = [[1,2,3,4,5],[7,9,0,1,2],[4,5,6,7,8],[0,1,2,3,4],[6,7,8,9,0]]

for i in A:
    print(i)
        
def boundary(A):
    ans = [] #using extra spaces to store the elements. we can just print the elements instead of storing as well. for my understanding
            #i am using extra space
    i = 0
    j = 0
    n = len(A)
    while n>1: #breaking condition is unitl my n is greater than 1 we keep prinint/appending
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
        n-=2
        i+=1
        j+=1
    if n ==1: #to handle edge case where we are not printing the middle most element. for odd n value
        ans.append(A[i][j])
    return ans
print(boundary(A))