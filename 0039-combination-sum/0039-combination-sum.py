class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        temp = []

        def cs(i: int, target: int):
            
            if target == 0: # tc
                combinations.append(temp[:])  # a copy of temp
                return
            if i == len(candidates): #tc
                return  
            if candidates[i] <= target:
                temp.append(candidates[i])
                cs(i, target - candidates[i])  
                temp.pop()  # Backtrack if it doesnt satisfy

            cs(i + 1, target)
        cs(0, target)
        return combinations
