'''
given a list of intervals and a merging interval we need to print the merging intervals in accending order 
if the intervals do not merge then print the interval given in the input
'''



def solution(intervals, s, e):

    n = len(intervals)

    for i in range(n):
        si = intervals[i][0]
        ei = intervals[i][1]

        if ei<s:
            print(si,ei)
        elif e<si:
            for j in range(i,n):
                print(intervals[j][0],intervals[j][1])
            return
        else:
            s = min(s,si)
            e = max(e,ei)
    print(s,e)