
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        if n <= 1:
            return 0  
        
        min_price = float('inf')
        max_price = 0

        for i in prices:
            if i <min_price:
                min_price = i
            elif i - min_price>max_price:
                max_price = i - min_price
        
        return max_price
