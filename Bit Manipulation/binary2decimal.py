''' Given a binary value, convert it to decimal value'''

A = 1011

def convert(A):
    ans = 0
    power = 0
    while A>0:
        temp = A%10
        ans += temp*(2**power)
        power+=1
        A = A//10
    return ans

print(convert(A))