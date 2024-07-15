'''
Given an integer array and an integer B, we need to find the minimum number of swaps required
to bring all the elements <= B together
'''

'''approach: first we need to find the number of elements that are <=B, and that will be our subarry size(window size)
after that we keep itterating though the sub arrays of that length and find the number of missing elements which are <=B, which we can call k
so them max k value subarry requires the minimum swaps.. and the final answer will be m-k swaps
'''

# A = [1,2,7,3,4,9,20,8,7,5]
# B = 8

A = [1,12,10,3,14,10,5]
B = 8
def minimumNumberOfSwaps(A,B):
    #finding number of elemets that are less <=B
    nums = 0
    for i in A:
        if i<=B:
            nums+=1
    s = 0
    e = nums-1
    k = 0
    while e<len(A)-1:
        temp =0
        #iterating through earh subarray and finding number of missing numbers <=B
        for i in range(s,e+1):
            if A[i]<=B: #this loop can be optimized.. we do not have to do this for every subarray
                temp+=1
        k = max(k,temp) #getting max k value
        s+=1
        e+=1
    return nums - k #answer

'''Optimization'''

'''
instead of running a loop again for each subarray, we are just checking the previous elemet and the new element are <=B and keep
varing the temp value
'''
def optimization(A,B):
    nums = 0
    for i in A:
        if i <=B:
            nums+=1
    k = 0
    for i in range(0,nums):
        if A[i]<=B:
            k+=1
    s = nums
    e = s+nums-1
    while e <len(A)-1:
        temp = k
        if A[s]<=B:
            temp -=1
        if A[e+1]<=B:
            temp+=1
        e+=1
        s+=1
        k = max(k,temp)
    return nums-k
print(minimumNumberOfSwaps(A,B))
print(optimization(A,B))