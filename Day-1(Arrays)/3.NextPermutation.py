# https://leetcode.com/problems/next-permutation/

def nextPermutation(nums):
    def swap(a,l,r):
        a[l],a[r] = a[r],a[l]
    
    def reverse(a,l,r):
        while l < r:
            swap(a,l,r)
            l+= 1
            r -= 1

        return a

    dec = len(nums)-2
    while(dec >= 0 and nums[dec] >= nums[dec+1]):
        dec -= 1

    print(dec)

    if dec >= 0:
        index = len(nums)-1
        while(nums[index] <= nums[dec]):
            index -= 1
        swap(nums, dec, index)

    reverse(nums, dec+1, len(nums)-1)

    return nums



print(nextPermutation([1,3,5,4,2]))
print(nextPermutation([5,4,3,2,1]))