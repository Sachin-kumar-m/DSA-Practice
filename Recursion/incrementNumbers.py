'''
given N, print all the numbers from 1 = N
'''

A = 4

def incrementNumbers(A):
    if A==0:
        return
    incrementNumbers(A-1) #we are calling this before print because we need to print in increasing order. this will keep decriminting and then
    #when the base case is satisfied. we then start prinint the numbers
    print(A)

incrementNumbers(A)