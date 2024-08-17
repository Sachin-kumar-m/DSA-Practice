'''
Given a string of length N, toggle each character,
if small=>captial, or if captial->small
'''


A = "sAchin"

def toggle(A):
    ans = ""
    for i in A:
        if ord(i)>=97 and ord(i)<=122:
            ans+=chr(ord(i)-32)
        elif ord(i)>=65 and ord(i)<90:
            ans+=chr(ord(i)+32)
    return ans

print(toggle(A))

# TC: O(N), we are traversing only one through the string
# SC : O(N), we are using extra space to store the answer