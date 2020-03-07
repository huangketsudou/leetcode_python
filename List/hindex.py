from typing import List
from collections import deque
import heapq
from heapq import heappush, heappop
import functools


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        nums=sorted(citations,reverse=True)
        n=len(nums)
        for i,h in enumerate(nums):
            if i+1>=h:
                return h
        return n


class Solution2:
    #桶排序
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        bucket = [0] * (n + 1)
        for citation in citations:
            if citation >= n:
                bucket[n] += 1
            else:
                bucket[citation] += 1
        #print(bucket)
        cur = 0
        for i in range(n, -1, -1):
            cur += bucket[i]
            if cur >= i:
                return i



k=Solution()
print(k.hIndex([3,0,6,1,5]))
