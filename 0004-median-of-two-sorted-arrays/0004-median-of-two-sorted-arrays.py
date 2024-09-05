
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        nums1.extend([0] * m)
        
        i, j, k = n - 1, m - 1, n + m - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
 
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        length = n + m
        if length % 2 == 1: 
            return nums1[length // 2]
        else:  
            mid = length // 2
            return (nums1[mid - 1] + nums1[mid]) / 2.0
