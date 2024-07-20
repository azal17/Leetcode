class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        
      
        dp = [[False] * n for _ in range(n)]
        
     
        longest = s[0]
        
     
        for i in range(n):
            dp[i][i] = True
        
      
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                longest = s[i:i + 2]
        

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    longest = s[i:j + 1]
        
        return longest
