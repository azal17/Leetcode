class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)

        count = 0
        element = None

        for i in range(n):
            if count ==0:
                count +=1
                element = nums[i]
            elif element == nums[i]:
                count +=1
            else:
                count -=1
        count1 = 0
        for i in range(n):
            if nums[i] ==element:
                count1 +=1
        if count1>(n/2):
            return element
        return -1 
  
       
                


        
        
        