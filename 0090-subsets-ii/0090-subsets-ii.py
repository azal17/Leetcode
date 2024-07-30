class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  
        result = []
        s = set()

        def sub(k: int, current: List[int]): 
            if k == len(nums):
               
                s.add(tuple(current))
                return
          
            current.append(nums[k])
            sub(k + 1, current)
           
            current.pop()
            sub(k + 1, current)
        
        sub(0, [])
        
       
        result = [list(t) for t in s]
        return result