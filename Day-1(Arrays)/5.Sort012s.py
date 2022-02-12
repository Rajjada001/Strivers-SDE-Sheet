# https://leetcode.com/problems/sort-colors/

def sortColors(a):
    i=j=0
    k = len(a)-1
    while j<=k:
        if a[j]==0:
            a[i],a[j]=a[j],a[i]
            i+=1
            j+=1
        elif a[j]==1:
            j+=1
        elif a[j]==2:
            # swap j and k
            a[j],a[k]=a[k],a[j]
            k-=1
    return a


print(sortColors([2,0,2,1,1,0]))
print(sortColors([2,0,1]))