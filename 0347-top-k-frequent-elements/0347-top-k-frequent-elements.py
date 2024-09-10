import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary_map = {}
        for i in nums:
            if i in dictionary_map:
                dictionary_map[i] += 1
            else:
                dictionary_map[i] = 1

        min_heap = []
        for i, freq in dictionary_map.items():
            heapq.heappush(min_heap, (freq, i))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        result = []
        while min_heap:
            freq, i = heapq.heappop(min_heap)
            result.append(i)
        
        return result
