#Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count1 = 0
        count2 = 0
        element1 = None
        element2 = None

        for i in range(n):
            if count1 ==0 and nums[i] != element2:
                element1 = nums[i]
                count1 +=1
            elif  count2 ==0 and nums[i] != element1:
                element2 = nums[i]
                count2 +=1
            elif element1 == nums[i]:
                count1 +=1
            elif element2 == nums[i]:
                count2 +=1
            else:
                count1 -=1
                count2 -=1
        
        c1 = 0
        c2 = 0
        for i in range(n):
            if nums[i] ==element1:
                c1 +=1
            elif nums[i] ==element2:
                c2 +=1
        
        if c1>n/3 and c2>n/3:
            return [element1,element2]
        elif c1 > n/3:
            return [element1]
        elif c2> n/3:
            return [element2]
        return []

        

