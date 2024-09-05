class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        k = n + m
        index2 = k // 2
        index1 = index2 - 1
        count = 0
        index1element, index2element = -1, -1

        i, j = 0, 0 
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                if count == index1:
                    index1element = nums1[i]
                if count == index2:
                    index2element = nums1[i]
                count += 1
                i += 1
            else:
                if count == index1:
                    index1element = nums2[j]
                if count == index2:
                    index2element = nums2[j]
                count += 1
                j += 1

        while i < n:
            if count == index1:
                index1element = nums1[i]
            if count == index2:
                index2element = nums1[i]
            count += 1
            i += 1

        while j < m:
            if count == index1:
                index1element = nums2[j]
            if count == index2:
                index2element = nums2[j]
            count += 1
            j += 1

        if k % 2 == 1:
            return index2element
        return (index1element + index2element) / 2.0
