A = [1,2,3,4,-4,-3,-2]

def equlIndex(A):
    pf = [0]*len(A)
    pf[0] = A[0]
    for i in range(1,len(A)):
        pf[i] = pf[i-1]+A[i]
    
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