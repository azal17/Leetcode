class Solution(object):
    def setZeroes(self, matrix):
        m = len(matrix) #length of rows 
        n = len(matrix[0]) #length of columns
        row,col = set(),set()

        if m < 1 or n >= 200 :
            return "Enter valid marix"

        
        for i in range(m):
            for j in range(n):
                
             if matrix[i][j] == 0:
                row.add(i)
                col.add(j)
        
        for i in row:
            for j in range(n):
                matrix[i][j] = 0

        for j in col:
            for i in range(m):
                matrix[i][j] = 0