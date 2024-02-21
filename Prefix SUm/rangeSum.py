#this is a modification for the prefix sum question
#given an array of n elements and  q querries, we need to find the sum of all the elements in the given query

arr = [-3,6,2,4,5,2,8,-9,3,1]

Q = [[4,8],[3,7],[1,3],[0,4],[6,9],[7,7]] #this is the list of all the querries and for each query we need to find the sum of total elements in that given range


#to solve this first we have create the prefix array and
#then we will iterate through the Q array and find the sum of ranged queries

#to find the prefix array
def prefixArray(arr):
    pf =[0]*len(arr)
    pf[0] = arr[0]
    for i in range(1,len(arr)):
        pf[i] = pf[i-1]+arr[i]  
    return pf

pfArray = prefixArray(arr) #here we are calculating the prefix array


#the following function will take the prefix array and the querries.

#the logic here is from the prefixed array to get the sum of a querry we can simply subtract the prfix sum of the right index with prefix 
# sum of the left-1 index. 
def rangedSum(prefixedArray,Q):
    ans = [0]*len(Q) #new answer array
    for i in range(len(Q)): #iterating throught the querris. 
        left = Q[i][0] #finding the left index
        right = Q[i][1] #finding the right index
        if left==0: # this is to handle edge case. if the left index is 0 we can directly use thr prefix value of right
            ans[i] = prefixedArray[right]
        else:
            ans[i] = prefixedArray[right] - prefixedArray[left-1] # if left is not zero then we can calcute the sum by pf[r]-pf[l-1]
    return ans

print(rangedSum(pfArray,Q))



