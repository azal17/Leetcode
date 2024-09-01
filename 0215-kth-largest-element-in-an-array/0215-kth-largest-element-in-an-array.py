import heapq
from typing import List
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
       min_heap = []
       n = len(nums)

       for i in range(n):
            heapq.heappush(min_heap, nums[i])
        
       while n > k:
            heapq.heappop(min_heap)
            n -= 1
       return  heapq.heappop(min_heap)
        


        