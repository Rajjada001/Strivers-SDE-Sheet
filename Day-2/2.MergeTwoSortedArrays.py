def mergeSortedArrays(a,b,m,n):
    i,j = m-1,n-1
    k = m+n-1

    while(i>=0 and j>=0):
        if a[i]>b[j]:
            a[k] = a[i]
            i-=1
        
        else:
            a[k]=b[j]
            j-=1
        k-=1

    if j>=0:
        a[:k+1] = b[:j+1]
    
    return a

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(mergeSortedArrays(nums1,nums2,m,n))