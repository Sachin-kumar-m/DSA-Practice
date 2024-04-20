#Given an array of length N, we need to find the length of smallest subarray which contains both min and max of the array


# a = [2,2,6,4,5,1,5,2,6,4,1]

a= [1,2,3,1,3,4,6,4,6,3]

# a= [8,8,8,8,8,8]


#brute force approach.
'''
we start from the right of the array and find the first min/max element, and again from that index loop over
to find the next max/min element. and calculate the length and get the minimum.

here the time complexity if O(N^2) and space is O(N)
'''
def smallestSubarray(a):
    n = len(a)

    result = n

    #finding the min and max values.
    maxElement = 0
    for i in a:
        if i>maxElement:
            maxElement = i
    minElement = maxElement
    for i in a:
        if i<minElement:
            minElement=i
    if minElement==maxElement:
        return 1

    #iterating from right to left and checking if the value is min or max
    for i in range(n-1,-1,-1):
        if a[i]==minElement: #if min is found. iterate again from i and get the immediate maxelement
            for j in range(i-1,-1,-1):
                if a[j] == maxElement:
                    counter = i-j+1
                    result = min(result,counter)
                    break
        elif a[i]==maxElement:
            for j in range(i-1,-1,-1):
                if a[j]==minElement:
                    counter = i-j+1
                    result =min(result,counter)
                    break
    return result


#time complexity : O(N^2) 
#space complexity : O(1), we are not using any extra space.

   

# Optimization:
'''
the approach is again iterate from the right. now if we find the min element, then we updatd the minIndex value and check the maxvalue on the 
left and update the maxIndex value. now if we find the min/max element again we keep updating the indices and calculating the result

while calculating the result. the newly updated value is the smaller value which can be used in calculating the result.

'''

def optimizedApproact(a):

    n = len(a)

    result = n
    maxElement = 0
    for i in a:
        if i>maxElement:
            maxElement = i
    minElement = maxElement
    for i in a:
        if i<minElement:
            minElement=i
    if minElement==maxElement:
        return 1
    maxIndex = -1
    minIndex = -1
    for i in range(n-1,-1,-1):
        if a[i]==minElement:
            minIndex = i
            if maxIndex!=-1:
                result = min(result,maxIndex-minIndex+1)
        elif a[i]==maxElement:
            maxIndex = i
            if minIndex!=-1:
                result = min(result,minIndex-maxIndex+1)
    return result
# print(optimizedApproact(a))

#time complexity : O(N)
#space complexity : O(1) 

