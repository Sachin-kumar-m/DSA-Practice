''''
given an array with just ones and zeros, we need to find the maximum length of 1s if we replace just one zero
'''

A = [1,1,1,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1]

def maxOnes(A):
    count = 0
    for i in range(len(A)):
        count+=A[i]
    if count == len(A):
        return 0
    elif count == 0:
        return 0
    ans = 0
    for i in range(len(A)):
        
        if A[i]==0: #whenever we find a 0, we then calculate the number of 1s on the left and on the right
            left = 0
            right = 0
            for j in range(i-1,-1,-1): #number of 1s on the left
                if A[j]==1:
                    left +=1
                else:
                    break
            for j in range(i+1,len(A)):#number of 1s on the right
                if A[j]==1:
                    right+=1
                else:
                    break
            ans = max(ans,left+right+1) #calculate the max ans
    return ans
print(maxOnes(A))

#Time Complexity : O(N), this is tricky, we are actully touching an element at most 3 times, which makes it 3 iterations,3N
#Space Complexity : O(1), we are not using extra space