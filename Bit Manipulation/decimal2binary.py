'''
given a decimal number, return its binary value
'''

A = 44

def convert(A):
    ans = ""
    while A>0:
        temp = A%2
        ans += str(temp)
        A//=2
    return ans[::-1]
print(convert(A))