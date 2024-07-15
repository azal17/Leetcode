from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()

        merge = []
        for i in range(n):
            if not merge or intervals[i][0] > merge[-1][1]:
                merge.append(intervals[i])
            else:
                merge[-1][1] = max(merge[-1][1],intervals[i][1])
        return merge




        