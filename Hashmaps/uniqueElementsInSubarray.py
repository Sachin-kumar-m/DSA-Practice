'''
Given an integer array, we need to find unique elements in the subarray ok size k
'''

'''
Approach: We can use the sliding window technique and also use hashmap to store the values of the subarray

when moving our window, we can check if the new element is present in our hashmap, if it is, we increase the 
frequency, if not we add it to our hashmap, 
we also check the exit element, if the frequency of the exit element is 1, then we remove that element entirely
if not we decrese the frequency value,
and then the length of the hashmap is our answer
we do this for every subarray of size k
'''

A = [2,4,3,8,3,9,4,9,4,10]

k = 4

def uniqueElementsInSubarray(A,k):
    frequencyMap = {}
    #first we iterate thourgh the first window and create our frequency map

    for i in range(k):
        if A[i] not in frequencyMap:
            frequencyMap[A[i]] = 1
        elif A[i] in frequencyMap:
            frequencyMap[A[i]]+=1
    print(len(frequencyMap))
    s = 1
    e = k
    while e<len(A):
        #checking the exit element, if the freq in more then 1 decrease the freq if not remove it entirely
        if frequencyMap[A[s-1]]==1:
            del frequencyMap[A[s-1]]
        else:
            frequencyMap[A[s-1]]-=1
        #now i want to check for the incoming element
        if A[e] in frequencyMap:
            frequencyMap[A[e]]+=1 #if the element is already present increase the frequency value, else add it to the hasmap
        else:
            frequencyMap[A[e]]=1
        print(len(frequencyMap))
        s+=1
        e+=1


uniqueElementsInSubarray(A,k)