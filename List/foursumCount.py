from typing import List
from collections import defaultdict


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        target = defaultdict(int)
        for i in C:
            for j in D:
                target[i + j] += 1
        ans=0
        for m in A:
            for n in B:
                ans+=target[-(m+n)]
        return ans

