import heapq

class MedianFinder:

    def __init__(self):
    
        self.min_heap = []
        self.max_heap = []
       
    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        
       

    def findMedian(self) -> float:
        if len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0])/2

# Usage:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
 