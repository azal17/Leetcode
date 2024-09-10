#T.C = O((kxn)log(kxn))+O((kxn)log(kxn)) = O((kxn)log(kxn)), S.C = O(kxn)
from sys import *
from collections import *
from math import *
import heapq

def mergeKSortedArrays(kArrays, k: int):
    min_heap = []
    

    for i in kArrays:
        for j in i:
            heapq.heappush(min_heap, j)
    
   
    result = []
    while min_heap:
        result.append(heapq.heappop(min_heap))
    
    return result