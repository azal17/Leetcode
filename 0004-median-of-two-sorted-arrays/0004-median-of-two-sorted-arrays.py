class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        k  = n + m

        index2 = k // 2
        index1 = index2 - 1
        cnt = 0
        index1_element, index2_element = -1, -1

        i, j = 0, 0
        while i < n and j < m:
            if nums1[i] < nums2[j]:
                if cnt == index1:
                    index1_element = nums1[i]
                if cnt == index2:
                    index2_element = nums1[i]
                cnt += 1
                i += 1
            else:
                if cnt == index1:
                    index1_element = nums2[j]
                if cnt == index2:
                    index2_element = nums2[j]
                cnt += 1
                j += 1

        while i < n:
            if cnt == index1:
                index1_element = nums1[i]
            if cnt == index2:
                index2_element = nums1[i]
            cnt += 1
            i += 1

        while j < m:
            if cnt == index1:
                index1_element = nums2[j]
            if cnt == index2:
                index2_element = nums2[j]
            cnt += 1
            j += 1

        if k % 2 == 1:
            return index2_element
        return (index1_element + index2_element) / 2.0
