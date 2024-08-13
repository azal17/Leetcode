from typing import List, Tuple

class Solution:
    def __init__(self):
        
        self.dp = [[None] * 31 for _ in range(101)]
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]: 
        def dfs(i: int, target: int) -> List[List[int]]:
            if target == 0:
                return [[]]
            if i == n or target < 0:
                return []
            if self.dp[i][target] is not None:
                return self.dp[i][target]
            
            x, m = nWm[i]
            result = []
            for j in range(m + 1):
                combinations = dfs(i + 1, target - j * x)
                for comb in combinations:
                    result.append([x] * j + comb)
            
            self.dp[i][target] = result
            return result
        freq = [0] * 51
        xMax = 0
        for x in candidates:
            freq[x] += 1
            xMax = max(xMax, x)
        nWm = []
        for x in range(1, xMax + 1):
            f = min(freq[x], target // x)
            if f > 0:
                nWm.append((x, f))
        n = len(nWm)
        self.dp = [[None] * (target + 1) for _ in range(n)]
        return dfs(0, target)
