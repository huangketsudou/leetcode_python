from typing import List
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums)
        result = 0
        for k,v in c.items():
            result += v*(v-1)//2
        return result


k=Solution()
print(k.numIdenticalPairs([1,1,1,1]))
