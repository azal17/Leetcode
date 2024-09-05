
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        result = []
        i, j = 0, 0
 
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        if i < n:
            result.extend(nums1[i:])
        if j < m:
            result.extend(nums2[j:])

        length = len(result)
        if length % 2 == 1:  
            return result[length // 2]
        else:  
            mid = length // 2
            return (result[mid - 1] + result[mid]) / 2.0
