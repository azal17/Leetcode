class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string = str(x)
        l = list(x_string)
        
        if l == l[::-1]:
            return True
        return False


        
        