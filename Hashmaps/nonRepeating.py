'''
given an integer array there are few non repeating elemts, return the first non repeating element
'''

A = [2,3,1,2,1,4,5,2]

def nonRepeating(A):
    temp = {}
    for i in A:
        if i in temp:
            temp[i]+=1
        else:
            temp[i] = 1
    
    for i in A: #iterating through the array because we need to find the first non repeating number
        if temp[i]==1:
            return i
    return -1
print(nonRepeating(A))