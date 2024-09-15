
class Solution:
    def canBePlaced(self, position: List[int], dist: int, n: int, balls: int) -> bool:
        last = position[0]
        cntBalls = 1 
        for i in range(1, n):
            if position[i] - last >= dist:
                cntBalls += 1
                last = position[i]
            if cntBalls >= balls:
                return True
        return False

    def maxDistance(self, position: List[int], m: int) -> int:
        n = len(position)
        position.sort()  
        left = 1 
        right = position[-1] - position[0] 
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if self.canBePlaced(position, mid,n, m):
                result = mid  
                left = mid + 1 
            else:
                right = mid - 1  
        
        return result
