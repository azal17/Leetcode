# for 3x3 matrix the solution will work
class Solution:
    
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        a = matrix

        for i in range(n):
            for j in range(n):
                if  i == 0:
                    if j == 0:
                        a[i][j],a[i][n-1] = a[i][n-1],a[i][j]
                    elif j != n-1:
                        a[i][j],a[j][j+1] =  a[j][j+1],a[i][j]
                elif j == 0 and i !=0 and i != n-1:
                    a[i][j],a[j][i] = a[j][i],a[i][j]
                elif i == n-1: 
                    if j == 0:
                      a[i][j],a[0][0] = a[0][0],a[i][j]
                    elif j != n-1:
                        a[i][j],a[j][0] = a[j][0],a[i][j]
                    elif j == n-1:
                         a[i][j],a[j][0] = a[j][0], a[i][j]
                   
