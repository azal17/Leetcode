# 3 loops and 1 hashset for the last element
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        my_set = set()

        for i in range(n):
            for j in range(i + 1, n):
                hashset = set()
                for k in range(j + 1, n):
                    sum_ijk = nums[i] + nums[j] + nums[k]
                    fourth_element = target - sum_ijk
                    if fourth_element in hashset:
                        new = tuple(sorted([nums[i], nums[j], nums[k], fourth_element]))
                        my_set.add(new)
                    hashset.add(nums[k])
                    
        
        result = [list(l) for l in my_set]
        return result
