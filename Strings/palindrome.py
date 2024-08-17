'''
Given a string, find out if its a palindrome or not
'''

A = "RACECAR"

def palindrome(A):
    start = 0
    end = len(A)-1

    while start<=end:
        if A[start]!=A[end]:
            return False   
        start+=1
        end-=1
    return True
print(palindrome(A))