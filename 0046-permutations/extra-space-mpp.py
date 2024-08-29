# T.C: n! x n , S.C: O(n) + O(n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        temp = []
        mpp = [0] * n 
        def perm():
            if len(temp) == n:
                ans.append(temp[:])
                return
            for i in range(n):
                if not mpp[i]:
                    temp.append(nums[i])
                    mpp[i] = 1 
                    perm() 
                    mpp[i] = 0  
                    temp.pop()  
        
        perm()
        return ans
