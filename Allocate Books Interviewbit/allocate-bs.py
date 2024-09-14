class Solution:
  
    def helper(self, array, mid_pages, n):
        students = 1 
        pages = 0  

        for i in range(n):
            if pages + array[i] <= mid_pages: 
                pages += array[i]
            else:
                students += 1 
                pages = array[i]  

        return students

    def books(self, A, B):
        n = len(A)

        if B > n:
            return -1
        
        low = max(A)  
        high = sum(A)  

        while low <= high:
            mid = (low + high) // 2  
            students = self.helper(A, mid, n) 

            if students > B:  
                low = mid + 1
            else:  
                high = mid - 1

        return low