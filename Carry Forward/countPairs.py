
"""
In a given array we need to find the count of pairs such that i<j
ex: we need to find the count of pairs a,g such that i<j

brute force will be to iterate thorugh the array twice and get the pair. but time complexity will be O(N^2)

to optimize this we can iterate from the right/end of the array, if we find 'g', increment the countG value,
and when we find 'a', then increment the ans by countG value. 

the number of g's on right of 'a' is the number of pairs that can be formed. So if we itertate form the right, 
we get the countG value and when we find 'a' we add the countG value to the actual answere

when we find 'a', then all the pairs that can be formed are the number of 'g's that are on the right of 'a',
this is why we come from right and get the count of G, and when we come across 'a' we just add the current count of g
to the ans, and keep doing it for all the a's that we find
"""

s = ['b','a','a','g','d','c','a','g']
# count the number of ag pairs in the above array

def countPairs(A):
    ans = 0
    countofG = 0 #initially count of g is 0
    n = len(A)
    for i in range(n-1,-1,-1): #iterating from right so we can get the count of g on the right of a
        if A[i]=='g':
            countofG+=1 #when we find 'g' we increment the count of G on the right
        if A[i]=='a':
            ans += countofG #when we find 'a', we add the countG value to the answere.
    return ans


    """
TIme complexity : O(N), since we are iterating only once through the array
Space Complexity: O(1), we are not using any extra space. 
    """