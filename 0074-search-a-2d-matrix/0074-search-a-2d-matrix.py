class Solution:
    def bS(self,nums: List[int],target: int)->bool:
        n = len(nums)
        low,high = 0,n-1

        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid +1
            else:
                high = mid-1
        return False

    def searchMatrix(self,matrix: List[List[int]],target: int):
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            if matrix[i][0] <= target <= matrix[i][m-1]:
                return self.bS(matrix[i],target)
        return False
    