class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        steps = m+n-2
        right = m-1
        down = n-1
        ans = 1

        for i in range(1,right+1):
            ans = ans*(steps-right+i)/i
        return int(ans)
        