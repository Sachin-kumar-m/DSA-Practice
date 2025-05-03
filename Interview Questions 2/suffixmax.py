'''
construct a suffix max array such that smax[i]= max of all the elements [0...i]

exapmle:

a=[1,-6,3,2,8,7]
now for i=0
max element from 0-1 is 1
for i = 1
max element from 0-i is 1 only because 1>-6
for i =2
max element fro 0-i is 3 because 3 is greater than 1 and -6

so final array = [1,1,3,3,8,8]
'''

def solution(A):
    pf = [0]*len(A)
    pf[0] = A[0]

    for i in range(1,len(A)):
        pf[i] = max(pf[i-1],A[i])
    return pf

A = [1,-6,3,2,8,7]

print(solution(A))

'''
Another variation of this problem can be given as 

find the suffix array such that surrixaray= max of all elements [i...n-1]

example:
arr = [3,10,6,7,0,2,-1]
now for i = 0
max element from 0-len(A)-1 is 10

for i =1
max element from 1-len(A)-1 is 10 again

for i = 2
max element from 2-len(A)-1 is 7, becuase 10 is out of our range and next biggest element is 7

final array = [10,10,7,7,2,2,-1]

approach : similar to the previous question but we itterate from end of the array

'''


def approach(A):
    n = len(A)
    pf=[0]*n
    pf[n-1] = A[n-1] #because the last element will always the same 

    #we iterate from the last element of the array

    for i in range(n-2,-1,-1):
        pf[i] = max(pf[i+1],A[i])
    
    return pf
A = [3,10,6,7,0,2,-1]
print(approach(A))

A = [4,8,-1,6,3]
print(approach(A))