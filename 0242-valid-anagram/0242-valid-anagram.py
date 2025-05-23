class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mpp = {}
        if len(s) != len(t):
            return False
        for i in s:
            mpp[i] = mpp.get(i, 0) + 1
        for j in t:
            if j not in mpp:
                return False
            mpp[j] -= 1
            if mpp[j] < 0:
                return False
        return True
        