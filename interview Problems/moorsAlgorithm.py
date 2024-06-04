'''
given an integer array we need to find a majority element,
an element is said to be a majority element if the occurance is more than n/2
'''

'''
approach: we keep finding 2 unique elements and removing them, following the moore's voting algorithm
'''

A = [4,6,5,3,4,5,6,4,4,4,4]

def majority(A):
    majorityElemet = None
    frequency = 0

    for i in range(len(A)):
        if majorityElemet == None:
            majorityElemet = A[i]
            frequency+=1
        elif majorityElemet == A[i]:
            frequency+=1
        else:
            frequency-=1
            if frequency==0:
                majorityElemet = None
        
    count = 0
    for i in range(len(A)):
        if A[i]==majorityElemet:
            count+=1
    if count>len(A)//2:
        return majorityElemet
    return False
print(majority(A))

'''
followup on this will be n/3 majority, then we need to delete 3 distinct elements
'''


