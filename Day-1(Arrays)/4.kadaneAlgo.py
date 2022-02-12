# https://leetcode.com/problems/maximum-subarray/
# max sub array in an array
def kadaneAlgo(a):
    currSum=MaxSum = 0
    for i in range(len(a)):
        currSum += a[i]
        currSum = max(currSum, a[i])
        MaxSum = max(MaxSum, currSum)
    
    return MaxSum


print(kadaneAlgo([-2,-1,6,-4,9,2]))