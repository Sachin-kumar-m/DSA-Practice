'''
given an array of integers, we need to find the frequency of the numbers
'''


A = [2,6,3,8,2,8,2,3,8,10,6]

q = [2,8,3,5]
def frequency(A,q):
    ans = {}
    for i in A:
        if i in ans:
            ans[i]+=1
        else:
            ans[i]=1
    freq = {}
    for i in q:
        if i in ans:
            freq[i] = ans[i]
        else:
            freq[i] = 0
    return freq

print(frequency(A,q))