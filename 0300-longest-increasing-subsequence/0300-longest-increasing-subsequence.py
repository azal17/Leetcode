import bisect

class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        
       
        tails = []
        
        for i in nums:
           
            l = bisect.bisect_left(tails, i)
          
            if l == len(tails):
                tails.append(i)
            else:
                
                tails[l] = i
        
       
        return len(tails)
