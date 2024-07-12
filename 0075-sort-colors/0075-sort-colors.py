class Solution(object):
    def sortColors(self, nums):
      
        a, b, c = 0, 0, 0

        
        for i in nums:
            if i == 0:
                a += 1
            elif i == 1:
                b += 1
            elif i == 2:
                c += 1

        
        for i in range(a):
            nums[i] = 0
        for i in range(a, a + b):
            nums[i] = 1
        for i in range(a + b, a + b + c):
            nums[i] = 2

        return nums

