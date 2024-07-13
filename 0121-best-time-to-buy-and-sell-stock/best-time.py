#using dictionary
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0 
        

        profit_dict: Dict[int, List[int]] = {}
        
        for i in range(n):
           
            future_days = []
            for j in range(i + 1, n):
                if prices[j] > prices[i]:
                    future_days.append(j)
            if future_days:
                profit_dict[i] = future_days
        
        
        max_profit = 0
        
        for day, future_days in profit_dict.items():
            current_price = prices[day]
            for future_day in future_days:
                potential_profit = prices[future_day] - current_price
                if potential_profit > max_profit:
                    max_profit = potential_profit
        
        return max_profit
