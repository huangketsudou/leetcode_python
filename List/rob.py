from typing import List
import functools
import math
import itertools


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:return 0
        n = len(nums)
        if n<2:return nums[0]
        dp=[0]*n
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        return dp[-1]


class Solution2:
    def rob(self, nums: List[int]) -> int:
        prevmax=0
        currmax=0
        for num in nums:
            tmp=currmax
            currmax=max(prevmax+num,currmax)
            prevmax=tmp
        return currmax


k=Solution2()
print(k.rob([1,7,9,4]))
