# https://leetcode.com/problems/set-matrix-zeroes/

def setZeroes(matrix):
    col_zero = 1
    rows,cols = len(matrix),len(matrix[0])

# 
    for row in range(rows):
        # if the first column contains zero, make the entire first column to zero
        if matrix[row][0]==0:
            col_zero=0
        for col in range(1,cols):
              if  matrix[row][col]==0:
                matrix[row][0] = matrix[0][col]=0
    
# traverse backwards
    for row in range(rows-1,-1,-1):
        for col in range(cols-1,0,-1):
            if matrix[row][0]==0 or matrix[0][col]==0:
                matrix[row][col]=0
        
        # if col zero is 0, then make that entire col to 0
        if col_zero==0:
            matrix[row][0]=0

    
    return matrix

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
            