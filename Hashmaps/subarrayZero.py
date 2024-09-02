'''
given an integer array, we need to find a subarray with sum=0
'''

A = [2,2,1,-3,4,3,1,-2,-3,2]


'''
Brute force would be to find sum of all the sub arrays and then check if any of them are zero
this would take O(n^2) since we have to generate all sub array sum
'''

def bruteForce(A):
    for i in range(len(A)):
        ans = 0
        for j in range(i,len(A)):
            ans+=A[j]
            if ans==0:
                return True
    return False

print(bruteForce(A))

# TC: O(N^2), we are generating sum of all the subarrays
# SC : O(1), we are not using any extra space

'''
Optimization: we can create a prefixSum array for the given array.
at an point if we find a duplite value in the prefixSum, then we know that the elements inbetween them add up to zero
also, if in the prefix array we find 0 then that  is also the ans
'''


def optimization(A):
    pf = [0]*len(A)
    pf[0]=A[0]
    for i in range(1,len(A)):
        pf[i] = pf[i-1]+A[i]
    
    s = set()
    for i in pf:
        if 0 in pf:
            return True
        else:
            s.add(i)
    if len(s)!=len(A):
        return True
    return False

print(optimization(A))

# TC: O(N), we are iterating through the array only once.
# SC: O(N), we are using extra space to create prefix array and also to create a new set