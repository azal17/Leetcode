class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True) 

        count = 0

        for i in boxTypes:
            if i[0] <= truckSize:
                count += i[1]*i[0]
                truckSize -= i[0]
            else:
                count += truckSize*i[1]
                break 
        return count
        