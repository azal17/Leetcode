class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n =len(candidates)
        candidates.sort()
        ans, temp = [],[]
        def cs(index: int, target: int):
            if target == 0:
                ans.append(temp[:])
                return
            if index == n:
                return

            for j in range(index, n):

                if j > index and candidates[j] == candidates[j-1]:
                    continue
                if target < candidates[j]:
                    break
                temp.append(candidates[j])
                cs(j+1, target - candidates[j])
                temp.pop()
        cs(0,target)
        return ans