

#this is again a variation to the prefix sum problem, here we need to find the equilibrium index, meaning for any index i the sum of
#elements on the left should be equal to sum of elements on the right. such an index is called equilbrium index
#to achive this we can first get the prefix array and then start iterating through the prefix array and find the sum of left and right 


A = [1,2,3,4,-4,-3,-2]


def equlIndex(A):

    #getting the prefix sum array
    pf = [0]*len(A)
    pf[0] = A[0]
    for i in range(1,len(A)):
        pf[i] = pf[i-1]+A[i]
    
    #iterating through the prefix array and finding the left and right sums and comparing it for each index
    for i in range(len(A)):
        left = 0 
        if i>0:
            left = pf[i-1]
        right = pf[len(A)-1]-pf[i]
        if i==len(A)-1:
            right = 0
        if left == right:
            return i
    return -1
print(equlIndex(A))

#time complexity : O(N) since we are iterating throught the array once in the original array and once in pf array O(N+N)=O(N)
#space complexity : O(N), sincw we are creating a prefix array of size N