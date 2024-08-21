class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        temp = []

        def isPalindrome(k: str) -> bool:
            return k == k[::-1] 

        def all(i: int, l: str):
            if i == len(l):
                result.append(temp[:])  
                return
            for j in range(i, len(l)):
                substring = l[i:j + 1]
                if isPalindrome(substring):
                    temp.append(substring)  
                    all(j + 1, l) 
                    temp.pop()  

        all(0, s) 
        return result
