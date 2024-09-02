'''
given an integer array, find the number of non duplicate elements,consider all the elements only once
'''


A = [3,5,6,5,4]
# A = [1,1,1,2,2]
# A = [3,3,3]
def nonDuplicate(A):
    freq = {}
    for i in A:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    
    return len(freq)

print(nonDuplicate(A))