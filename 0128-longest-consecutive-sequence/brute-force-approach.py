class Solution:
    
    def linearSearch(nums: List[int], n: int, x: int) -> bool:
        for i in range(n):
            if nums[i] == x:
                return True
        return False

    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        longest_sequence = 1

        for i in range(n):
            x = nums[i]
            count = 1

            while Solution.linearSearch(nums, n, x + 1):
                x += 1
                count += 1

            longest_sequence = max(longest_sequence, count)
        
        return longest_sequence
