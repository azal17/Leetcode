

class Solution:
    def countPairs(self, nums: List[int], low: int, mid: int, high: int) -> int:
        right = mid + 1
        count = 0
        for i in range(low, mid + 1):
            while right <= high and nums[i] > 2 * nums[right]:
                right += 1
            count += (right - (mid + 1))
        return count
    
    def mergeSort(self, nums: List[int], low: int, high: int) -> int:
        count = 0
        if low < high:
            mid = (low + high) // 2
            count += self.mergeSort(nums, low, mid)
            count += self.mergeSort(nums, mid + 1, high)
            count += self.countPairs(nums, low, mid, high)
            nums[low:high + 1] = sorted(nums[low:high + 1])
        return count
    
    def reversePairs(self, nums: List[int]) -> int:
        return self.mergeSort(nums, 0, len(nums) - 1)

