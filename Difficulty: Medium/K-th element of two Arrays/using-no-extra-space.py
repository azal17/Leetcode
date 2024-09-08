
class Solution:
    def kthElement(self, k, arr1, arr2):
        n = len(arr1)
        m = len(arr2)
        

        k -= 1
        
        i, j = 0, 0
        count = 0
        
        while i < n and j < m:
            if arr1[i] < arr2[j]:
                if count == k:
                    return arr1[i]
                count += 1
                i += 1
            else:
                if count == k:
                    return arr2[j]
                count += 1
                j += 1
        
        while i < n:
            if count == k:
                return arr1[i]
            count += 1
            i += 1
        
        while j < m:
            if count == k:
                return arr2[j]
            count += 1
            j += 1
        

        return -1
