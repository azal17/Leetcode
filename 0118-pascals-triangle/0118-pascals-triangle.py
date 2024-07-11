class Solution(object):
    def generate(self, numRows):
        if numRows <= 0:
            return []

        a = [[0] * (i + 1) for i in range(numRows)]


        for i in range(numRows):
            a[i][0] = 1
            a[i][-1] = 1

   
        for i in range(2, numRows):
            for j in range(1, i):
                a[i][j] = a[i - 1][j - 1] + a[i - 1][j]

        return a



