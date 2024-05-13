''''
given an array with just ones and zeros, we need to find the maximum length of 1s if we swap zero with existing one in the array
'''

'''
Approach, first calculate the number of ones in the array,then we iterate through the array when we find an element as zero, 
then we calculate the number of ones on the left 
and then number of ones on the right
if left+right=count of 1s, then there is no extra 1 in the array which can be used to swap

else, we have an exta 1 which can be used to swap. 

in first scenario, ans = max(ans, left+right)
in second scenario, ans = max(ans, left+right+1)
'''
A = [0,1,1,1,0,1,1,0,0]
def swap(A):
    count = 0
    for i in range(len(A)):
        if A[i]==1:
            count+=1
    ans = 0
    for i in range(len(A)):
        if A[i]==0:
            left = 0
            right = 0
            for j in range(i-1,-1,-1): #calculate number of 1s on the left
                if A[j]==1:
                    left+=1
                else:
                    break
            for j in range(i+1,len(A)):#calculate number of 1s on the right
                if A[j]==1:
                    right+=1
                else:
                    break
            if left+right == count:
                ans = max(ans, left+right)
                
            else:
                ans = max(ans, left+right+1)
                
    return ans

print(swap(A))


#Time complexity: O(N), we have break conditions so each element will be visited 3 times. so 3N iterations
#Space Complexity: O(1), not using extra space