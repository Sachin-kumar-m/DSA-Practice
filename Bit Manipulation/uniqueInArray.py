'''
given an array of length n, which has only one unique element in it. Return that unique element
'''

A = [1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,9]

def unique(A):
    ans = {}
    for i in A:
        if i in ans:
            ans[i]+=1
        else:
            ans[i] = 1
    for i in ans:
        if ans[i]==1:
            return i
    return ans
print(unique(A))


# we can do this in O(N) time and O(1) space by simply applyting XOR on every element

def optimization(A):
    ans = A[0]
    for i in range(1,len(A)):
        ans = ans ^ A[i]
    return ans
print(optimization(A))

