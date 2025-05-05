'''given an array of length n, find total sum of all the subarrays'''

A = [6, 8 ,-1, 7]

def sumofallsubarrays(A):
    result = 0
    for i in range(len(A)):
        summ = 0
        for j in range(i,len(A)):
            summ+=A[j]
            result+=summ
    return result

print(sumofallsubarrays(A))

# time Complexity: O(N^2)
# space Complexity: O(1)



'''optimization, we can calculate the occurance of each element and then muliply the occurance with the element and that should give 
us the answere

calculate the occurance of ith: (i+1)*(n-i) for matrix problem we use (i+1)*(n-i)*(j+1)*(m-j) 
'''
def optimization(A):
    n = len(A)
    result = 0
    for i in range(len(A)):
        temp = (i+1)*(n-i)*A[i]
        result+=temp
    return result
print(optimization(A))

# time complexity: O(N)
# space Complexity: O(1)