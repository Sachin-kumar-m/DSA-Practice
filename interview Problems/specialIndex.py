'''
given an integer array of length N, we need to find the count of special indices.

Special Index : if the element in the given index is removed and the sum of even indexes = sum of odd indexes then that index is 
called special index
'''

'''
Approach: we initially populate the evenPrefix and oddPrefix array. and when i is removed. all the even elements after i will be treated
as odd and all the odd are treated even. 
'''

A = [4,3,2,7,6,-2]
def specialIndex(A):
    oddSum = [0]*len(A)
    evenSum = [0]*len(A)

    oddSum[0] = 0
    evenSum[0] =A[0]
    for i in range(1,len(A)):
        if i%2==0:
            evenSum[i] = evenSum[i-1]+A[i]
            oddSum[i] = oddSum[i-1]
        else:
            evenSum[i] = evenSum[i-1]
            oddSum[i] = oddSum[i-1]+A[i]
    ans = 0
    for i in range(len(A)):
        odd = 0
        even = 0
        if i==0:
            odd = oddSum[len(A)-1]
            even = evenSum[len(A)-1] - evenSum[0]
        else:
            odd = oddSum[i-1]+(evenSum[len(A)-1]-evenSum[i])
            even = even[i-1]+(odd[len(A)-1]-odd[i])
        if odd == even:
            ans+=1
        return ans

print(specialIndex(A))

#Time Complexity : O(N), 
#Space Complexity: O(N), we are creating prefix arrays of length N


