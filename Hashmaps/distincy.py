'''
given an integer arry we need to find if all the elemnts in the array are distinct are not
'''


A = [1,2,3,4,5,10,7,8,9]

def distinct(A):
    s = set()
    for i in A:
        s.add(i)
    if len(s)==len(A):
        return True
    return False
print(distinct(A))