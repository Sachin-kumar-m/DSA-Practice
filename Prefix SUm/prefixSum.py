
#  here we are trying to calclulate the prefix sum of an array
# Given an array of length n, we need to return an array where arr[i] = [a[0]+a[1]+1[2]....a[i]]

#to achive the result we can follow this approach. we can safely say pf[0] = A[0] since the first element will always be the same
# and then iterate through the given array and find sum at each index and add that value to the new array


def prefixArray(arr):
    pf = [0]*len(arr)

    pf[0] = arr[0] #as the frist element will always be same as the first element of the give array

    #now we have to iterate though the given array and find the sum for each index
    for i in range(1,len(arr)):#iterating from 1 because we already have value for the 0th index
        pf[i] = pf[i-1]+arr[i]  #here we can use the previos sum already present in the pf array to calculate the next sum
    return pf
arr = [5,10,1,2,6]
print(prefixArray(arr))




