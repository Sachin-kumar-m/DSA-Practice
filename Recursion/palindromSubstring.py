'''
given a string with a starting and ending index, we need to check if the substring is a palindrome or not using recursion
'''


A = "gooddad"
s = 4
e = 6
def palindrome(A,s,e):
    if s>=e:
        return
    if A[s]==A[e]:
        return True
    else:
        return False
    return palindrome(A,s+1,e-1)

print(palindrome(A,s,e))