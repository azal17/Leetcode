class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix, suffix = [0]*n , [0]*n
        prefix[0] = height[0]

        for i in range(1, n):
            prefix[i] = max( prefix[i-1], height[i])
        suffix[n-1] = height[n-1]

        for i in range(n-2, -1, -1):
            suffix[i] = max(suffix[i+1], height[i])
        count = 0

        for i in range(n):
            count += min(prefix[i], suffix[i]) - height[i]
        return count
