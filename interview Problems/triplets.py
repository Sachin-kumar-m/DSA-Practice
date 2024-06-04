'''
given an array of length N, we need find number of triplets such that i<j<k and A[i]<A[j]<A[k]
'''

'''
Approach : for any element we find the number of smaller elements on the left and number of greater elements on the right
the multiple of right*left will give me the number of triplets that can be formed for that particula index.

and the number of triplets it will form will be multiple of right*left 
and we keep calculating this for every element and adding it to our final answere
'''

def trip(A):    
    ans = 0
    for i in range(1,len(A)):
        left = 0
        right = 0
        for j in range(i-1,-1,-1):
            if A[j]<A[i]:
                left+=1
        for k in range(i+1,len(A)):
            if A[k]>A[i]:
                right+=1
        ans+=(right*left)
    return ans
A = [4,1,2,6,9,7]
print(trip(A))

