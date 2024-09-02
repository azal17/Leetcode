class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        numbers = []
        for i in range(1, n + 1):
            fact *= i
            numbers.append(i)

        k -= 1
        fact //= n
        
        ans = ""
        
        while numbers:
            index = k // fact
            ans += str(numbers.pop(index))
            if not numbers:
                break
            k %= fact
            fact //= len(numbers)
        
        return ans

        
         