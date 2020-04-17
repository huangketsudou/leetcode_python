from typing import List



class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #对每一个数字检验其最右边界，当右边界小于数组长度时，不可达
        start = 0
        end = 0
        n = len(nums)
        while start <= end and end < len(nums) - 1:
            end = max(end, nums[start] + start)
            start += 1
        return end >= n - 1


class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        #start = 0
        n = len(nums)
        start = n - 2
        end = n - 1
        while start >= 0:
            if start + nums[start] >= end: end = start
            start -= 1
        return end <= 0


k=Solution()
print(k.canJump([3,0,8,2,0,0,1]))
