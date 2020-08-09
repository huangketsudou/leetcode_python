from typing import List


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        prev = {0}
        cur = 0
        res = 0
        for n in nums:
            cur += n
            if cur-target in prev:
                res +=1
                prev ={0}
                cur=0
            else:
                prev.add(cur)
        return res



k = Solution()
print(k.maxNonOverlapping(nums=[-2, 6, 6, 3, 5, 4, 1, 2, 8], target=10))
