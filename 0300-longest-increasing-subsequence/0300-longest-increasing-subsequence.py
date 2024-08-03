import bisect

class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        
       
        tails = []
        
        for num in nums:
           
            idx = bisect.bisect_left(tails, num)
          
            if idx == len(tails):
                tails.append(num)
            else:
                
                tails[idx] = num
        
       
        return len(tails)
