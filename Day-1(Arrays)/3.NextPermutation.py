# https://leetcode.com/problems/next-permutation/

def swap(a,l,r):
    temp = a[l]
    a[l] = a[r]
    a[r] = temp

def reverse(a, l, r):
    while(l<r):
        a[l],a[r] = a[r],a[l]
        l+=1
        r-=1
    

def nextPermutation(a):
    if len(a)<=1:
        return
    # find the decrement
    dec = len(a)-2
    while(dec >= 0 and a[dec]>= a[dec+1]):
        dec-=1
    
    print(dec)
    
    if dec >= 0:
        index = len(a)-1
        while(a[index] <= a[dec]):
            index -= 1
        swap(a,dec,index)
    
    # if the condition fails just reverse the array
    reverse(a, dec+1, len(a)-1)

    return a


print(nextPermutation([1,3,5,4,2]))
print(nextPermutation([5,4,3,2,1]))