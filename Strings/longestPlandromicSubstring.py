'''
Given a string of length N, find the longest panlindromic substring
'''


'''
Approach: we create an expand function which will take 2 pointer, and then move along in opposite direction unil S[p1] != S[p2]
and return the length travelled by p1 and p2

we do this expand for even and odd length of string
for odd p1=p2=i
for even p1=i and p2=i+1
'''

def expand(S,p1,p2):
    while p1>=0 and p2<len(S) and S[p1]==S[p2]:
        p1-=1
        p2+=1
    return p2-p1-1 #because the lenght is p2-p1+1 and since p1 and p2 are 2 index ahead we subtact 2, which is p2-p1+1-2

def longestPalindromicSubstring(S):
    ans = 0
    for i in range(0,len(S)):
        ans = max(ans, expand(S,i,i))
    for i in range(0,len(S)):
        ans = max(ans, expand(S,i,i+1))
    return ans

S = "abcbabcbabcba"
# print(len(S))
print(longestPalindromicSubstring(S))

# TC: O(N^2), since we have expand function which take O(N) time and call it inside so N^2 solution, this can also be solved by Dynamic Programming
#also Manacher’s Algorithm will be used to solve this in linear time
#SC : O(1), we are not using any extra space