'''
Bubble sorting algorithm : for every iteration, placing one element to its correct positions is known as bubble sort

'''

A = [8,2,4,1,3,5,9,6,7,0]
def bubbleSort(A):
    for i in range(1,len(A)):
        for j in range(0,len(A)-1):
            if A[j]>A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
    return A

print(bubbleSort(A))

# TC : O(N^2), for every iteration we are putting on element in correct place. so to put n-1 elemetnts it take n iteration, so N^2 complexity


def decendingOrder(A):
    for i in range(1,len(A)):
        for j in range(0,len(A)-1):
            if A[j]<A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
    return A


    # comparator function in python
def comparator():
    return None
A.sort(key = comparator)