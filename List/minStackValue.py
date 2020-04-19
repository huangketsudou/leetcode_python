from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        n=len(nums)
        cumsum=[0]*n
        for i in range(n):
            cumsum[i]=cumsum[i-1]+nums[i]
        minimun=min(cumsum)
        return 1 if minimun>=0 else 1-minimun


    