#we can use dutch flag approach (3 pointers)
class Solution(object):
    def sortColors(self, nums):
        n = len(nums)

        low = 0 #starting index for both,assuming the array is completely unsorted
        mid = 0
        end = n-1

        while mid<=end:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid],nums[low]
                low+=1
                mid+=1
            elif  nums[mid] == 1:
                mid+=1
            else:
                nums[mid],nums[end] = nums[end],nums[mid]
                end -=1

        return nums
