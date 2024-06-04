'''
given an interger array of length n and Q queries, for each query we are given 2 indices (S,E)

For every Query return the sum of all even indexes of the elements in the range S to E
'''

'''
Approach : we can use prefix sum technique, and in our prefix array we only add if its a even index, 
and then use the range query (extended version of prefix sum) technique to find the sum of the given queries
'''


A = [2,3,1,6,4,5]
Q = [[1,3],[2,5],[0,4],[3,3]]

def evenIndexSum(A,Q):
    prefixArray = [0]*len(A)
    prefixArray[0] = A[0]

    for i in range(1,len(A)):
        if i%2==0: #if index is even then only i add my current index value
            prefixArray[i] = prefixArray[i-1]+A[i] 
        else: #if not i will keep the previous value
            prefixArray[i] = prefixArray[i-1]
    
    ans = [0]*len(Q)

    #here is simple range sum technique
    for i in range(len(Q)):
        s = Q[i][0]
        e = Q[i][1]
        if s==0:
            ans[i] = prefixArray[e]
        else:
            ans[i] = prefixArray[e]-prefixArray[s-1]
    return ans


print(evenIndexSum(A,Q))

# Time Complexity : O(N+Q), we are iterating through the array and also the Query
# Space Complexity : 0(N+Q), we are using extra space to populate the prefixArray and also i am using an Array of len(Q) to store my answers