class Solution:
    def findUnique(self, arr):
        # code here 
        mpp = {}
        for i in arr:
            mpp[i] = mpp.get(i, 0) + 1
        for i in arr:
            if mpp[i] == 1:
                return i