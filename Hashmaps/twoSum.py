'''
given an array, we need find a pair where A[i]+A[j] = k, where i!=j
'''

'''
Brute Force: we can take one element each time and check the pairs and see if the sum adds up to the target
'''

A = [1,2,3,4,5,6,7]
k = 3
def pairSum(A,k):
    for i in range(len(A)):
        b = k - A[i]
        for j in range(i+1,len(A)):
            if A[j]==b:
                return [i,j]
    return False

print(pairSum(A,k))


# TC: O(N^2), we have 2 loops
# SC: O(1), we are not using extra space


"""
Optimization : in the second loop we are tring to find if we have B(k-A[i]) in the given array,
so for every element we can calculate the B and check if we have it in our array, 
we can create an hashmap with all the elements in the array and check if b(k-A[i]) is available in the hashmap, 
also we need to make sure i!=j, so to check this condition, we can check if a==b then check the frequency of a in the hashmap
"""

def optimization(A,k):
    freq = {}
    for i in A:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    
    for i in range(len(A)):
        b = k - A[i]
        if b in freq:
            if A[i]==b:#checking if the element is same 
                if freq[A[i]]>1: #if same we are checking its frequency, and if frequency is more than 1 
                    return True
            else:
                return True
    return False

print(optimization(A,k))


'''
Now they might ask us to return the indices of these 2 elements
same approach as above, this time we are storing the numbers and its indexes in an hashmap,
then we check if the compliment is present in the hashmap, if yes then we return the indexes.
'''
A = [3,2,4]
k = 6
def indexes(A,k):
    hashmap = {}
   
    for i in range(len(A)):
        # compliment = k - A[i]
        if A[i] not in hashmap:
            hashmap[A[i]] = i
    for i in range(len(A)):
        compliment = k - A[i]
        if compliment in hashmap and i!=hashmap[compliment]: #second condition is to check if its not the same index or number
            
            return [i,hashmap[compliment]]
    return False
   
print(indexes(A,k))

# we can do this using sets

def twoSumUsingSets(A,k):
    s = set()
    for i in range(len(A)):
        compliment = k - A[i]
        if compliment in s: #we are checking if the compliment is in our sets. and A[i] only if its not in the set this is to avoide same number sum
            return True
        else:
            s.add(A[i])
    return False
print(twoSumUsingSets(A,k))
