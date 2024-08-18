'''
given a string with all lower case characters, sort the string in accending order
'''


A = 'bdabacdb'

def sorting(A):
    count = [0]*256
    for i in range(len(A)):
        temp = ord(A[i])
        count[temp]+=1
    ans = ""
    for i in range(len(count)):
        if count[i]!=0:
            for j in range(count[i]):
                ans+=chr(i)
    return ans
print(sorting(A))