class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        if n > m:
            return self.findMedianSortedArrays(nums2, nums1)
        
        left = (n + m + 1) // 2 
        low, high = 0, n
        
        while low <= high:
            mid1 = (low + high) // 2
            mid2 = left - mid1
          
            l1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            r1 = nums1[mid1] if mid1 < n else float('inf')
            l2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            r2 = nums2[mid2] if mid2 < m else float('inf')

            if l1 <= r2 and l2 <= r1:
                if (n + m) % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                high = mid1 - 1
            else:
                low = mid1 + 1
        
        return 0.0  
