class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        r = []
        unique_quadruplets = set()
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        num = nums[i] + nums[j] + nums[k] + nums[l]
                        if target == num:
                            result = tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))
                            if result not in unique_quadruplets:
                                unique_quadruplets.add(result)
                                r.append(list(result))
        
        return r
