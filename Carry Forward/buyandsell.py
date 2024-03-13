'''
Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Return the maximum possible profit.
'''

A = [2,1,3,4,5,1,2,7,8,4,5]

def stock(A):
    minPrice = A[0]
    maxProfit = 0
    for i in range(1,len(A)):
        if A[i]<minPrice:
            minPrice = A[i]
            minDay = i
        else:
            maxProfit = max(maxProfit,A[i]-minPrice)
            

    return maxProfit

print(stock(A))

#Time Complexity : O(N)
#Space Complexity : O(1) since we are using constant space. 