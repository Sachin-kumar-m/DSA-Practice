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


'''
this can also be done without using if statements, we can use bit manipulation, 

so if we represent A in bits -> 01000001
if we set the 5th bit then that will be like adding 32, which eventually be small "a"

so based on this theory. if we set the bit then its converted to small case, if we unset the bit then
it will be converted to capital case
'''

def bitManipulation(A):
    ans = ""
    for i in range(len(A)):
        ans += chr(ord(A[i]) ^ (1<<5))    
    return ans
print(bitManipulation(A))