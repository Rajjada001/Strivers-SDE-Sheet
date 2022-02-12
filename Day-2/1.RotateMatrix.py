def rotateMatrix(a):
        def swap(a,i,j):
                a[i][j],a[j][i] = a[j][i],a[i][j]
        
        def reverse(a):
            l,r = 0,len(a)-1
            while(l<r):
                a[l],a[r] = a[r],a[l]
                l+=1
                r-=1
                
        for i in range(len(a)):
            for j in range(i):
                swap(a,i,j)
                print(a)
        
        for i in range(len(a)):
            reverse(a[i])

        return a

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(rotateMatrix(matrix))
                