class Solution:
    def check(self, quantities, mid, store, n):
        s = 0
        for i in range(n):
            quan = quantities[i]
           
            while quan > 0:
                if quan >= mid:
                    quan -= mid
                    s += 1
                else:
                    s += 1
                    quan = 0
            
                if s > store:
                    return False
        return True

    def minimizedMaximum(self, store, quantities):
        n = len(quantities)
        right = max(quantities) 
        res = -1
        left = 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if self.check(quantities, mid, store, n):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return res
