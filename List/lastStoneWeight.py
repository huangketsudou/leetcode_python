from typing import List
from heapq import heapify,heappop,heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i]=-stones[i]
        heapify(stones)
        while len(stones)>2:
            maximun,submaximun=heappop(stones),heappop(stones)
            if maximun-submaximun>0:
                heappush(stones,maximun-submaximun)
        return sum(stones)
