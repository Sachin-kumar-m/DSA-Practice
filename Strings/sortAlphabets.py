'''
given a string with all lower case characters, sort the string in accending order
'''


'''
Approach : we have just 26 alphabets so we can store number of ocurance in an array.
and then iterate and add those occurance of the alphabet
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

# TC: O(N), we are traversing through the string once. other traversal is of contant space so total will be o of N
# SC: O(N), we are creating a new string also we are creating an array of length 256, so total will be O of N