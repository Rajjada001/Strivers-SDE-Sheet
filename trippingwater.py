def trippingWater(a):
    res = 0
    l,r = 0,len(a)-1
    lMax,rMax = 0,0

    while l<=r:
        if a[l]<=a[r]:
            if a[l]>lMax:
                lMax = a[l]
            else:
                res += lMax - a[l]
            l+=1
        else:
            if a[r]>rMax:
                rMax = a[r]
            else:
                res += rMax - a[r]
            r-=1
    return res

print(trippingWater([5,0,6,2,3]))