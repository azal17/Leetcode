class Solution:
    def longestPalindrome(self,s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        longest = ""

        for i in range(n):
            for j in range(i, n):
                substring = s[i:j + 1]
                if is_palindrome(substring) and len(substring) > len(longest):
                    longest = substring

        return longest
