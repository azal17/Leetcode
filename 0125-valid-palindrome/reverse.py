class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()  
        n = len(s)
        i = n - 1
        reversedstr = ""
        cleaned = ""

        while i >= 0:
            if s[i].isalnum():
                reversedstr += s[i]
            i -= 1

        for c in s:
            if c.isalnum():
                cleaned += c

        return cleaned == reversedstr

