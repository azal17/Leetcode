class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       n = len(nums)

       if  n == 0:
        return 0

       l = 1
       s = set()

       for i in range(n):
        s.add(nums[i])

       for i in s:
        if i-1 not in s:
            count = 1
            x = i
            while x+1 in s:
                count +=1
                x +=1
            l = max(l,count)
       return l

