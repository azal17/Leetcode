# Time complexity : O(n^2) -> nested loop , Space Complexity = O(1) -> no additional space
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        count = 0
        for i in range(n):
            j = i
            leftMax = 0
            rightMax = 0
            while j >= 0:
                leftMax = max(leftMax, height[j])
                j -= 1
            j = i
            while j < n:
                rightMax = max(rightMax, height[j])
                j += 1
            count = count+ (min(leftMax, rightMax) - height[i])
        return count
